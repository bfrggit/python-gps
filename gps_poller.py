import threading
from threading import Thread
import time
from gps import *

class GPSPoller(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.gpsd = gps(mode = WATCH_ENABLE)
	
	def run(self):
		while True:
			self.gpsd.next()
	
	def lat(self):
		return self.gpsd.fix.latitude
	
	def lon(self):
		return self.gpsd.fix.longitude
	
	def alt(self):
		return self.gpsd.fix.altitude
	
	# Ground speed (m/sec)
	def speed(self):
		return self.gpsd.fix.speed
	
	# Climb rate (m/sec)
	def climb(self):
		return self.gpsd.fix.climb

	# Course over ground from true north (deg)
	def track(self):
		return self.gpsd.fix.track
	
	# UTC time string
	# def utc(self):
	# 	return self.gpsd.utc
	
	# Estimated longitude error (m)
	def epx(self):
		return self.gpsd.fix.epx

	# Estimated latitude error (m)
	def epy(self):
		return self.gpsd.fix.epy

	# Estimated vertical error (m/sec)
	def epv(self):
		return self.gpsd.fix.epv
	
	# Estimated speed error (m/sec)
	def eps(self):
		return self.gpsd.fix.eps

	# Estimated course error (deg)
	def epd(self):
		return self.gpsd.fix.epd

	# Estimated time-stamp error (sec)
	def ept(self):
		return self.gpsd.fix.ept

	# Fix mode
	def mode(self):
		return self.gpsd.fix.mode

	MODE_STR = {
		0: "NO DATA",
		1: "NO FIX",
		2: "2D FIX",
		3: "3D FIX"
	}

	def dict(self):
		return {
			"lat": self.lat(),
			"lon": self.lon(),
			"alt": self.alt(),
			"speed": self.speed(),
			"climb": self.climb(),
			"track": self.track(),
			"epx": self.epx(),
			"epy": self.epy(),
			"epv": self.epv(),
			"eps": self.eps(),
			"epd": self.epd(),
			"ept": self.ept(),
			"mode": self.mode()
		}

MAIN_SLEEP = 1

if __name__ == "__main__":
	poller = GPSPoller()
	poller.daemon = True
	poller.start()
	while True:
		print poller.dict()
		time.sleep(MAIN_SLEEP)
