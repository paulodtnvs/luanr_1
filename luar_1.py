#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import ephem
from datetime import datetime
from ephem import Sun, Observer, pi, hours, degrees
import time
import math


def main():
	ta =time.localtime()	
	sp = ephem.Observer()	
	sp.lat = ephem.degrees('-23:32:00')   # your latitude
	sp.lon = ephem.degrees('-46:38:00')   # your longitude
	ra, dec = sp.radec_of('0', '-90')
	sp.date = '2022/%i/%i %i:%i:%i' % (ta[1], ta[2], ta[3], ta[4], ta[5])
	ephem.now = sp.date
	m = ephem.Moon()
	m.compute(sp)
	s=ephem.Sun()
	s.compute(sp)
	
	print (' Lunar time:', hours(( ra - m.ra) % (2 * pi)))
	
	print  (' Earth Time:', '{}:{}:{}'.format(ta[3],ta[4],ta[5]))
	
	print ('==============================')

	

	
	time.sleep(60)
	main()
	
	
if __name__ == '__main__':
    main()
