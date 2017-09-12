from SpeakPython.SpeakPythonRecognizer import SpeakPythonRecognizer;
import RPi.GPIO as GPIO
import time
import pygame
import udp
file_ryoukai = 'sound/ryoukai.mp3'
file_hai = 'sound/hai.mp3'
file_cmdinvalid = 'sound/invalidcmd.mp3'
file_konni = 'sound/konnichiwa.mp3'
file_init = 'sound/init.mp3'
file_wakatta = 'sound/wakatta.mp3'
file_iterashai = 'sound/iterashai.mp3'
file_okaeri = 'sound/okaeri.mp3'
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
pygame.init()
pygame.mixer.init()
def playsound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)
def blinkled(pin,n,delay):
    x = 0
    while x < n:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        if n > 1:
            time.sleep(delay)
        x = x+1
def execute(input_str):    
    print input_str
    blinkled(4,2,0.25);
    if "on" in input_str:
        playsound(file_ryoukai)
        udp.main("on")
    if "off" in input_str:
        playsound(file_ryoukai)
        udp.main("off")
    if "I am home" in input_str:
        playsound(file_okaeri)
    if "I am out" in input_str:
        playsound(file_iterashai)
playsound(file_init)
print "ready"
recog = SpeakPythonRecognizer(execute, "megumi")
recog.setDebug(1);
stop = False
try:
	while not stop:
		recog.recognize();
except KeyboardInterrupt:
	stop = True;
	print "Interrupted.";
finally:
        GPIO.cleanup();
