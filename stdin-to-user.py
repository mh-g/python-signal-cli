#!/usr/bin/python3
# (c)2017 mh-g
# usage:
# echo "Hello World" | ./std-in-to-user.py 

from pydbus import SystemBus

import sys

data = sys.stdin.read()

bus = SystemBus()

signal = bus.get('org.asamk.Signal', object_path='/org/asamk/Signal/_OWN_ACCOUNT')
# replace OWN_ACCOUNT with your local phone number (without leading '+' sign)

signal.sendMessage(data, [], '+___USER___')
# replace ___USER___ with the corresponding phone number
