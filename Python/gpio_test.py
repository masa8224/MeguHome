import RPi.GPIO as GPIO
import time
import udp
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
A=0
while True:
    while not GPIO.input(17):
        time.sleep(0.01)
    CURRENT_STATE = 1
    if A == 0:
        udp.udp("on")
        print "ON!"
        A = 1
    elif A == 1:
        udp.udp("off")
        print "OFF"
        A = 0
    while GPIO.input(17) == CURRENT_STATE:
        time.sleep(0.01)
    CURRENT_STATE = 0
