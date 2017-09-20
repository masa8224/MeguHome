import time
import sys
import pygame
import udp
import RPi.GPIO as GPIO
from SpeakPython.SpeakPythonRecognizer import SpeakPythonRecognizer
VOICE_RYOUKAI = 'sound/ryoukai.mp3'
VOICE_HAI = 'sound/hai.mp3'
VOICE_CMDINVALID = 'sound/invalidcmd.mp3'
VOICE_KONNI = 'sound/konnichiwa.mp3'
VOICE_INIT = 'sound/init.mp3'
VOICE_WAKATTA = 'sound/wakatta.mp3'
VOICE_ITERASHAI = 'sound/iterashai.mp3'
VOICE_OKAERI = 'sound/okaeri.mp3'
VOICE_JAA_NE = 'sound/jaane.mp3'
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN) #Status LED
GPIO.setup(17, GPIO.OUT) #Test push button. pls ignore
pygame.init()
pygame.mixer.init()
STOP = False
ACTIVE = True

def playsound(file_voice):
    """play sound!"""
    pygame.mixer.music.load(file_voice)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def blinkled(pin, n, delay):
    """Blinking the LEDs"""
    x = 0
    while x < n:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        if n > 1:
            time.sleep(delay)
        x = x + 1

def execute(input_str):
    """Excute the commands!"""
    #print input_str
    blinkled(17, 2, 0.25)
    exec input_str
def ignore(status):
    """Ignoring the voice commands!"""
    global ACTIVE
    if status is True:
        ACTIVE = False
        print "deactivate"
        print ACTIVE 
    if status is False:
        ACTIVE = True
        print "activate"
def on(light):
    if ACTIVE is True:        
        playsound(VOICE_WAKATTA)
        udp.main("on")
def off(light):
    print ACTIVE
    if ACTIVE is True:        
        playsound(VOICE_WAKATTA)
        udp.main("off")
def Iam(home):
    if ACTIVE is True:        
        if home == "home":
            playsound(VOICE_OKAERI)
        if home == "going":
            playsound(VOICE_ITERASHAI)
def quit():
    global STOP
    if ACTIVE is True:        
        STOP = True
        playsound(VOICE_JAA_NE)
        sys.exit()

playsound(VOICE_INIT)
RECOG = SpeakPythonRecognizer(execute, "megumi")
print "ready!"
#RECOG.setDebug(1)
try:
    while not STOP:
        RECOG.recognize()
except KeyboardInterrupt:
    STOP = True
    print "Interrupted."
finally:
    GPIO.cleanup()