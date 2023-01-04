import json
import machine
import time
import picozero

#with open('env.json', 'r') as f:
#    config = json.load(f)

sr04 = picozero.DistanceSensor(echo=17, trigger=16, max_distance=5)

def callback_log_distance(t):
    dist = sr04.value
    print(f"dist: {dist}")
    
# Perform reset every 10min
#reset = machine.Timer(-1)
#reset.init(period=1000*60*10, mode=machine.Timer.ONE_SHOT, callback=callback_reset)

#try:
#    ip, mac = pico.wifi_connect(config['wifi'])
#    mqttc = pico.mqtt_connect(config['mqtt'])
#    pico.mqtt_serve(mqttc, mac)
#except Exception as e:
#    print(e)
#    machine.reset()

while True:
    pass
