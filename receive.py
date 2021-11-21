#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging
from gpiozero import LED
from send_mail import *
from rpi_rf import RFDevice

rfdevice = None
red = LED(12)
a = time.time()
b = 0
counter = 0

# pylint: disable=unused-argument
def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=27,
                    help="GPIO pin (Default: 27)")
args = parser.parse_args()

signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()
timestamp = None
logging.info("Listening for codes on GPIO " + str(args.gpio))
while True:
    if rfdevice.rx_code_timestamp != timestamp:
        timestamp = rfdevice.rx_code_timestamp
        if len(str(rfdevice.rx_code))> 0:
              counter += 1
              print(counter)
              while (b<5):
                     red.on()
                     time.sleep(1)
                     red.off()
                     b = time.time()-a
              b=0
              print('data received')
              if counter == 5:
                     send_message()
                     counter = 0
    time.sleep(0.01)
rfdevice.cleanup()
