import speech_recognition as sr
import RPi.GPIO as GPIO
GPIO.output()
r = sr.Recognizer()
with sr.Microphone(device_index=2) as source:
    r.adjust_for_ambient_noise(source, duration=3)
    print "Say something!"
    audio = r.listen(source, phrase_time_limit=5)
    print "done"
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))
