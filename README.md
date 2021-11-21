# 433-fixed-code-hacking
# This project is about fixed key (on-off-keying) and rolling jam attaque (which i couldn't do it cause i don't have sufficient money to buy advanced tools)
# pre-requests:
# Raspberry-Pi 
# RTL-SDR (optional - to intercept and analyse the signals)
# 433Mhz Tx/Rx (basic costs about 5$) 
# Documentation and time to read


This project is used to intercept and re-produce the same signal to the target to simulate the function of the original remote key (replay attack).
It has also an option to bruteforce to try all possible combination of a binary code, \
if we know just the length of the key which is pretty much easy using an rtl-sdr
(there are scripts that decode directly the intercepted signal and show the binary code in your terminal)
This project contains uses also a led that light up if the number of essais equal to 5 (means 5 attemps to crack the signal) 
And then it send the owner an email adress to inform him that someone is trying to bruteforce his car....

The bruteforce here is used as a jammer, we don't care about what code we sent, all we care about is to keep the receiver busy 
so we can try intercepting the key while its jammed for some secondes (as long as takes till we get at least two or three signals)



here is the youtube video demonstrating how this works !!!
