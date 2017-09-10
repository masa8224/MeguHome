import RPi.GPIO as GPIO
import subprocess
import time
import pygame
file_ryoukai = 'sound/ryoukai.mp3'
file_hai = 'sound/hai.mp3'
file_cmdinvalid = 'sound/invalidcmd.mp3'
file_init = 'sound/init.mp3'
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
playsound(file_init)
while True:
    while not GPIO.input(17):
        time.sleep(0.01)
    print "Listening..."
    CURRENT_STATE = 1
    playsound(file_hai)
    GPIO.output(4,GPIO.HIGH)
    proc = subprocess.Popen("voicecommand",stdout=subprocess.PIPE)
    
    while True:
      line = proc.stdout.readline()
      if line != '':        
        if line.rstrip() == "No translation" or line.rstrip() == "Could not find answer. Try again.":
            print "Invalid command"
            playsound(file_cmdinvalid)
            blinkled(18,2,0.25)
        else:
            print line.rstrip()            
            playsound(file_ryoukai)
            blinkled(18,1,1)
      else:
        break
    GPIO.output(4,GPIO.LOW) 
    while GPIO.input(17) == CURRENT_STATE:
        time.sleep(0.01)
    CURRENT_STATE = 0

