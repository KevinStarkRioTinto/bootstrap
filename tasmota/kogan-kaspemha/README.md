
# Kogan Smart Plug with Energy Meter

![](https://user-images.githubusercontent.com/5904370/55288894-d8574380-53be-11e9-9738-0a801b0705b5.png)

https://www.kogan.com/au/buy/kogan-smarterhome-smart-plug-with-energy-meter-pack-of-4-kogan/

https://help.kogan.com/hc/en-us/articles/360044496173

## Tuya Convert

https://tasmota.github.io/docs/Tuya-Convert/
https://github.com/ct-Open-Source/tuya-convert

On `tuya-convert` host:
- Ubuntu 18.04
- rufus 3.11 portable
- Run with `sudo`
- Flash with bundled `tasmota.bin`

On mobile/other device:
- Connect to `tasmota-nnnn` hotspot
- Configure wifi:
  `Backlog SSID1 <myssid>; Password1 <mypassword>`

On server:
- Find IP of new host on network and connect
- Clear all settings except Wifi/MQTT  
  `Reset 6`
- Update firmware:
  - To latest 8.x:  
    `OtaUrl http://ota.tasmota.com/tasmota/release-8.5.1/tasmota.bin`  
    `Upgrade 1`
  - To latest 9.x:  
    `OtaUrl http://ota.tasmota.com/tasmota/release-9.1.0/tasmota.bin.gz`  
    `Upgrade 1`
  - To latest:  
    `OtaUrl http://ota.tasmota.com/tasmota/release/tasmota.bin.gz`  
    `Upgrade 1`

- Apply `other` configuration
  - https://templates.blakadder.com/kogan-KASPEMHA.html
  - `{"NAME":"Kogan KASPEMHA","GPIO":[17,0,0,0,133,132,0,0,131,56,21,0,0],"FLAG":0,"BASE":18}`

- Power calibration: https://tasmota.github.io/docs/Power-Monitoring-Calibration/
  - `VoltageSet {123.0}`
  - `PowerSet {123.0}`
  - `CurrentSet {123.0}`  
    Calculate as `(power/voltage)*1000`
