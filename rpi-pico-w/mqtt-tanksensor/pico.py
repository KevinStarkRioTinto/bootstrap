import network
import ubinascii
import socket
from time import sleep
import picozero
import machine
import umqtt.simple
import json
import time

onboard_led = machine.Pin("WL_GPIO0", machine.Pin.OUT)

def wifi_connect(config):
    #Connect to WLAN
    onboard_led.on()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print(wlan.scan())
    wlan.connect(**config)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    onboard_led.off()
    uid = ubinascii.hexlify(machine.unique_id()).decode()
    ip = wlan.ifconfig()[0]
    mac = ubinascii.hexlify(wlan.config('mac'), ':').decode().upper()
    print(f'{uid} connected on {ip} as {mac}')
    #print(wlan.config('ssid'))
    #print(wlan.config('hostname'))
    return ip, mac

def get_sensors():
    return {
        "temperature": picozero.pico_temp_sensor.temp,
    }

def mqtt_connect(config):
    client = umqtt.simple.MQTTClient(**config)
    client.connect()
    return client
    
def mqtt_serve(mqttc, mac):
    mac = mac.replace(':', '-')
    while True:
        onboard_led.on()
        topic = f"pico/{mac}/state"
        msg = json.dumps(get_sensors())
        print({"topic": topic, "msg": msg})
        mqttc.publish(topic, msg)
        onboard_led.off()
        time.sleep_ms(10*1000)
