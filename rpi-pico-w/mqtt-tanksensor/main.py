import json
import machine
import network
import ubinascii
import socket
import picozero
import time

# Configure 
onboard_led = machine.Pin("WL_GPIO0", machine.Pin.OUT)

# Load configuration variables
with open('env.json', 'r') as f:
    config = json.load(f)

def callback_reset(t):
    print("reset()")
    machine.reset()
    
# Perform reset every 10min
reset = machine.Timer(-1)
reset.init(period=1000*60*10, mode=machine.Timer.ONE_SHOT, callback=callback_reset)


nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect(**config['wifi'])
while nic.isconnected() == False:
    print('Waiting for connection...')
    time.sleep(1)
onboard_led.off()
uid = ubinascii.hexlify(machine.unique_id()).decode()
ssid = nic.config('ssid')
ip = nic.ifconfig()[0]
mac = ubinascii.hexlify(nic.config('mac'), ':').decode().upper()
hostname = nic.config('ssid')
print(f'{uid} connected to {ssid} at {ip} ({mac})')

rssi=-99
for nw in nic.scan():
    if nw[0].decode() == ssid:
        rssi = max(rssi, nw[3])
print({"rssi": rssi})

#try:
#    ip, mac = pico.wifi_connect(config['wifi'])
#    mqttc = pico.mqtt_connect(config['mqtt'])
#    pico.mqtt_serve(mqttc, mac)
#except Exception as e:
#    print(e)
#    machine.reset()

