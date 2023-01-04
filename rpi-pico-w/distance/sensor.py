import json
import machine
import time
import picozero
import logging
import dht20
import os

handler = logging.FileHandler('sensor.log')
logger = logging.getLogger(__name__)
logger.addHandler(handler)

#with open('env.json', 'r') as f:
#    config = json.load(f)

i2c0_sda = machine.Pin(8)
i2c0_scl = machine.Pin(9)
i2c0 = machine.I2C(0, sda=i2c0_sda, scl=i2c0_scl)

dht = dht20.DHT20(0x38, i2c0)
sr04 = picozero.DistanceSensor(echo=13, trigger=12, max_distance=2.0)
sr01_active = machine.Pin(11, mode=machine.Pin.OUT, value=1)

sensors = { }
def callback_measure_distance(t):
    sensors['distance_m'] = sr04.distance
    logger.info(json.dumps({"distance_m": sensors['distance_m']}))
    
def callback_measure_temperature(t):
    meas = dht.measurements
    if not meas['crc_ok']:
        print("dht CRC failed")
        return
    
    sensors['temperature_c_onboard'] = picozero.pico_temp_sensor.temp
    logger.info(json.dumps({
        "temperature_onboard_c": sensors['temperature_c_onboard']
    }))
    
    sensors['temperature_c'] = meas['t']
    sensors['relative_humidity'] = meas['rh']
    
    logger.info(json.dumps({
        "temperature_c": meas['t'],
        "relative_humidity": meas['rh'],
    }))
    
    
timer_distance = machine.Timer()
timer_distance.init(period=1000, mode=machine.Timer.PERIODIC, callback=callback_measure_distance)

timer_dht = machine.Timer()
timer_dht.init(period=5000, mode=machine.Timer.PERIODIC, callback=callback_measure_temperature)

print(os.uname())
while True:
    print(str(time.localtime()), sensors)
    time.sleep(1)