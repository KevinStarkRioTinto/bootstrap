# Tasmota Profiles

This directory stores device configuration profiles for Tasmota-flashed smart-home devices. They can be configured interactively using a web interface, http endpoint or MQTT topic.

The [`tasmota-setup`](tasmota-setup.py) script simplifies this process of sending configuration commands to the devices using python `requests` library against the http endpoint.

## Power Calibration

```sh
tasmota-calibrate.py --from-ip [ip] to_ip [to_ip]
```
