import threading
from threading import Thread
import time
import os
from gps import *

class GPSPoller(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.gpsd = gps(mode = WATCH_ENABLE)
	
	def run(self):
		while True:
			self.gpsd.next()
	
	def latitude(self):
		return self.gpsd.fix.latitude
	
	def longitude(self):
		return self.gpsd.fix.longitude
	
	def altitude(self):
		return self.gpsd.fix.altitude
	
	def eps(self):
		return self.gpsd.fix.eps
	
	def epx(self):
		return self.gpsd.fix.epx

	def epv(self):
		return self.gpsd.fix.epv
	
	def ept(self):
		return self.gpsd.fix.ept
	
	def speed(self):
		return self.gpsd.fix.speed
	
	def climb(self):
		return self.gpsd.fix.climb

	def track(self):
		return self.gpsd.fix.track

	def mode(self):
		return self.gpsd.fix.mode
	
	def utc(self):
		return self.gpsd.utc

MAIN_HD_SP = 15
MAIN_SLEEP = 1.0

if __name__ == "__main__":
	poller = GPSPoller()
	poller.daemon = True
	poller.start()
	while True:
		os.system("clear")
		print "GPS readings"
		print
		print ("%%-%ds") % MAIN_HD_SP % ("latitude"),  poller.latitude()
		print ("%%-%ds") % MAIN_HD_SP % ("longitude"), poller.longitude()
		print ("%%-%ds") % MAIN_HD_SP % ("altitude"),  poller.altitude()
		print ("%%-%ds") % MAIN_HD_SP % ("eps"),       poller.eps()
		print ("%%-%ds") % MAIN_HD_SP % ("epx"),       poller.epx()
		print ("%%-%ds") % MAIN_HD_SP % ("epv"),       poller.epv()
		print ("%%-%ds") % MAIN_HD_SP % ("ept"),       poller.ept()
		print ("%%-%ds") % MAIN_HD_SP % ("speed"),     poller.speed()
		print ("%%-%ds") % MAIN_HD_SP % ("climb"),     poller.climb()
		print ("%%-%ds") % MAIN_HD_SP % ("track"),     poller.track()
		print ("%%-%ds") % MAIN_HD_SP % ("mode"),      poller.mode()
		print ("%%-%ds") % MAIN_HD_SP % ("time"),      poller.utc()
		time.sleep(MAIN_SLEEP)
