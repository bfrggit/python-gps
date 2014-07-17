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

if __name__ == "__main__":
	poller = GPSPoller()
	poller.daemon = True
	poller.start()
	print "Daemon starting..."
	time.sleep(2)
	while True:
		os.system("clear")
		print "GPS readings"
		print
		print ("%%-%ds") % 15 % ("latitude"),  poller.latitude()
		print "%-15s" % ("longitude"), poller.longitude()
		print "%-15s" % ("altitude"),  poller.altitude()
		print "%-15s" % ("eps"),       poller.eps()
		print "%-15s" % ("epx"),       poller.epx()
		print "%-15s" % ("epv"),       poller.epv()
		print "%-15s" % ("ept"),       poller.ept()
		print "%-15s" % ("speed"),     poller.speed()
		print "%-15s" % ("climb"),     poller.climb()
		print "%-15s" % ("track"),     poller.track()
		print "%-15s" % ("mode"),      poller.mode()
		print "%-15s" % ("time"),      poller.utc()
		time.sleep(1)

