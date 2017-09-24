#!/usr/bin/python3
# (c)2017 mh-g

def msgRcv (timestamp, source, groupID, message, attachments):
   print ("msgRcv called")
   print (message)
   return

from pydbus import SystemBus
from gi.repository import GLib

bus = SystemBus()
loop = GLib.MainLoop()

signal = bus.get('org.asamk.Signal')

signal.onMessageReceived = msgRcv
loop.run()
