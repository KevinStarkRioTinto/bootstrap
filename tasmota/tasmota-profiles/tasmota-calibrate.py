#!/usr/bin/env python3

import argparse
import requests
import logging
import json
import time

from urllib.parse import urlencode, quote_plus
from pprint import pprint
import http.client as http_client

version = "0.0.1.9000"

logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.WARN)

def get_tasmota_power_calibration(ip):
    url = f'http://{ip}/cm'
    cal = {}
    r = requests.get(url, params = { 'cmnd': 'Status0' }, timeout = 1)
    r.raise_for_status()
    mac = r.json()['StatusNET']['Mac']

    for cmnd in ['VoltageCal', 'PowerCal', 'CurrentCal']:
        r = requests.get(url, params = { 'cmnd': cmnd }, timeout = 1)
        r.raise_for_status()
        cal[cmnd] = r.json()[cmnd]

    return {mac: cal}

def set_tasmota_relay(ip, state, timeout=1, sleep=None):
    url = f'http://{ip}/cm'
    r = requests.get(url, params = { 'cmnd': f'Power {"1" if state else "0"}' }, timeout = timeout)
    r.raise_for_status()
    if sleep: time.sleep(sleep)
    return r.json()['POWER'] == 'ON'

def set_tasmota_power(ip, Voltage, Power, **kwargs):
    url = f'http://{ip}/cm'
    r = requests.get(url, params = { 'cmnd': f'Backlog VoltageSet {int(Voltage)}; PowerSet {int(Power)}; CurrentSet {int((Power/Voltage)*1000)}' }, timeout = 1)
    r.raise_for_status()
    return r.json()

def get_tasmota_power(ip, timeout=1):
    url = f'http://{ip}/cm'
    r = requests.get(url, params = { 'cmnd': 'Status0' }, timeout = timeout)
    r.raise_for_status()
    r = r.json()
    return r['StatusSNS']['ENERGY']

if __name__ == "__main__":
    # Command line 
    parser = argparse.ArgumentParser(description="Calibrate power readings between two or more linked tasmota devices")
    parser.add_argument("--from-ip", help = "IP to source power readings from")
    parser.add_argument("--from-saved", help = "JSON file to load existing calibration settings from")
    parser.add_argument("to_ip", help = "IP to set power calibration for", nargs='+')

    # Parse and validate the supplied arguments
    args = parser.parse_args()

    pprint(args.from_ip)
    pprint(args.to_ip)

    assert set_tasmota_relay(args.from_ip, True, timeout=10)
    for ip in args.to_ip:
        assert set_tasmota_relay(ip, True, timeout=10)
    
    # Let power spike settle
    time.sleep(3)

    # if args.from_ip:
    #     print("calibration:", get_tasmota_power_calibration(args.from_ip))

    obs = get_tasmota_power(args.from_ip)
    for ip in args.to_ip:
        print(ip)
        set_tasmota_power(ip, **obs)
        pprint(get_tasmota_power_calibration(ip))

    # Send voltage calibration for each device, wait
        # VoltageSet {123.0}
    # Send power calibration for each device, wait
        # PowerSet {123.0}
    # Send current calibration for each device
        # CurrentSet {(power/voltage)*1000}
    # Capture MAC address and calibration details to file. 

    # Turn power OFF