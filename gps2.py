import math
import serial
import threading
import time

GPSPosition = {'time': '00:00:00', 'lat': 0.0, 'lon': 0.0, 'alt': 0, 'sats': 0, 'fixtype': 0}

class GPS(Object):
    """
       This is a replacement for the gps.py script included with skygate.
       The GPS forthat file appears to require a Ublox chipset, and be 
       a HAT.  This one is for usingthe BU-353S4 USB GPS
    """

    def __init__(self, Device='/dev/ttyUSB0'):
        self.ser = serial.Serial(Device,4800, timeout=1)

 
    def __gps_thread(self):

        Line = ''

        while True:
            gps_raw = self.ser.readline()
            if "*" in gps_raw:
                gps_split = gps_raw.split('*')
