#!/usr/bin/python3

import argparse
import requests
import logging
import json
from collections import OrderedDict
from urllib.parse import urlencode, quote_plus
from pprint import pprint
import http.client as http_client

version = "0.0.1.9000"

logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.WARN)

# Command line 
parser = argparse.ArgumentParser(description="Write or read setup configuration commands to a tasmota flashed device")
parser.add_argument("-n", "--name", help = "Override the device name assigned in the profile(s)")
parser.add_argument("ip", help="IP address of device", default="192.168.1.999")
parser.add_argument("-v", "--verbose", help="Increase the verbosity", action="count", default=0)
parser.add_argument("profile", help = "Name of json file(s) to load as commands for batch execution", nargs='*')
parser.add_argument('--version', action='version', version=f'%(prog)s {version}')

# Parse and validate the supplied arguments
args = parser.parse_args()

if args.verbose > 1: print(args)
if args.verbose > 1: 
    logger.setLevel(logging.DEBUG)
    http_client.HTTPConnection.debuglevel = 1
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

# Test the device connectivity and validate
if args.verbose: print(f"IP:       {args.ip}")
url = f'http://{args.ip}/cm'
try:
    r = requests.get(url, params = { 'cmnd': 'Status' }, timeout = 1)
    r.raise_for_status()
    r = r.json()
except requests.exceptions.RequestException as e:
    print(e)
    exit()

pprint(r)

if args.profile:
    # Load the profiles and validate
    cmnd = ""
    for p in args.profile:
        pcommands = json.load(open(p, 'r'))
        for pc in pcommands:
            if pc.keys() >= {"command", "value"}:
                cmnd = f"{cmnd}{pc['command']} {pc['value']};"

    if len(cmnd):
        cmnd = f"Backlog {cmnd}"
        print(cmnd)
        try:
            r = requests.get(url, params = {'cmnd': cmnd}, timeout = 10)
            r.raise_for_status()
            r = r.json()
        except requests.exceptions.RequestException as e:
            print(e)
            exit()
