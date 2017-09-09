import RPi.GPIO as GPIO
import subprocess
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
while True:
    while not GPIO.input(17):
        time.sleep(0.01)
    print "Listening..."
    CURRENT_STATE = 1
    GPIO.output(4,GPIO.HIGH)
    proc = subprocess.Popen("voicecommand",stdout=subprocess.PIPE)
    
    while True:
      line = proc.stdout.readline()
      if line != '':        
        if line.rstrip() == "No translation" or line.rstrip() == "Could not find answer. Try again.":
            print "Invalid command"
            GPIO.output(18, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(18, GPIO.LOW)
            time.sleep(0.25)
            GPIO.output(18, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(18, GPIO.LOW)
        else:
            print line.rstrip()
            GPIO.output(18, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(18, GPIO.LOW)
      else:
        break
    GPIO.output(4,GPIO.LOW) 
    while GPIO.input(17) == CURRENT_STATE:
        time.sleep(0.01)
    CURRENT_STATE = 0

