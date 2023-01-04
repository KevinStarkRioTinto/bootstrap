import json
import machine
import pico

with open('env.json', 'r') as f:
    config = json.load(f)

def callback_reset(t):
    print("reset()")
    machine.reset()
    
# Perform reset every 10min
reset = machine.Timer(-1)
reset.init(period=1000*60*10, mode=machine.Timer.ONE_SHOT, callback=callback_reset)

try:
    ip, mac = pico.wifi_connect(config['wifi'])
    mqttc = pico.mqtt_connect(config['mqtt'])
    pico.mqtt_serve(mqttc, mac)
except Exception as e:
    print(e)
    machine.reset()

