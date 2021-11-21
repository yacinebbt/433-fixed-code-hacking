from gpiozero import LED
import time
from receive import *


def notify_user():
	red = LED(12)
	a = time.time()
	b = 0
	while (b<60):
	    b=time.time()-a
	    red.on()
	    # print('googd')
	    time.sleep(1)
	    red.off()
	    # print('non')
	    time.sleep(1)

#notify_user()
