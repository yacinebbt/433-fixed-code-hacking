import os
import sys
from rpi_rf import *

gpio = 17
o = RFDevice(gpio)
o.enable_tx()

def send_10(rawcode):
	for i in range(len(rawcode)):
		if rawcode[i] == '0':
			o.tx_l0()
#			o._sleep((rawcode.count('1') * o.tx_pulselength) / 1000000)
		else:
			o.tx_l1()
#			o._sleep((rawcode.count('0') * o.tx_pulselength) / 1000000)
		#o._sleep(100)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		rawcode = str(sys.argv[1])
		send_10(rawcode) 
	else:
		print('Syntaxe: python3 replay_signa.py BINARY_CODE')

'''
#	print(sys.argv[1])
#	rawcode = '0111110000010'

#	t = 0
	for i in range(992,993):
		i = bin(i)[2:]
		if len(str(i)) < 10:
			i = '0'+str((10-len(str(i)))*'0')+str(i)+'10'
#			print(i)
			send_10(i)
			o._sleep(t)
#			o.tx_bin(i)
		else:
			i = '0'+str(i)+'10'
			print(i)
#			o.tx_bin(i)
			send_10(str(i))
			o._sleep(t)

'''
