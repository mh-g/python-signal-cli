#!/usr/bin/python3
# (c)2017 mh-g
# usage:
# echo "Hello World" | ./stdin-to-group.py

from pydbus import SystemBus

import sys

data = sys.stdin.read()

bus = SystemBus()

signal = bus.get('org.asamk.Signal')

signal.sendGroupMessage(data, [], [___GROUP___])
# replace ___GROUP___ with byte-representation of 
# e.g. 0x01, 0x23,  0x45, 0x67,  0x89, 0xab,   0xcd, 0xef,   0x01, 0x23,   0x45, 0x67,   0x89, 0xab,   0xcd, 0xef
# obtain these bytes by:
# grep "groupId" ___SIGNAL_CONFIG_FILE___
# where ___SIGNAL_CONFIG_FILE___ is the signal configuration stored in .config/signal/data/
# echo ___BASE64_REPRESENTATION___ | base64 --decode | hexdump -x
# where ___BASE64_REPRESENTATION___ is the string stored in that line
# and splitting the two-byte words into single bytes
