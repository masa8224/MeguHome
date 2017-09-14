from SpeakPython.SpeakPythonRecognizer import SpeakPythonRecognizer
import RPi.GPIO as GPIO
import pygame
import udp
import time
import sys
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
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
pygame.init()
pygame.mixer.init()
STOP = False

def playsound(file_voice):
    pygame.mixer.music.load(file_voice)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def blinkled(pin, n, delay):
    x = 0
    while x < n:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        if n > 1:
            time.sleep(delay)
        x = x + 1


def execute(input_str):
    print input_str
    blinkled(4, 2, 0.25)
    exec input_str
def on(light):
    udp.main("on")
def off(light):
    udp.main("off")
def Iam(home):
    if home == "home":
        playsound(VOICE_OKAERI)
    if home == "going":
        playsound(VOICE_ITERASHAI)
def quit():
    STOP = True
    playsound(VOICE_JAA_NE)
    sys.exit()

playsound(VOICE_INIT)

RECOG = SpeakPythonRecognizer(execute, "megumi")
print "ready!"

try:
    while not STOP:
        RECOG.recognize()
except KeyboardInterrupt:
    STOP = True
    print "Interrupted."
finally:
    GPIO.cleanup()