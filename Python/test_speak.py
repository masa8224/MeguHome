from SpeakPython.SpeakPythonRecognizer import SpeakPythonRecognizer;
import time
import udp
#define callback function with 1 parameter (string)
def execute(s):
        print s;
        if "on" in s:
                udp.main("on")
        if "off" in s:
                udp.main("off")

#creates recognition instance
#param 1 - function accepting 1 string argument - used as callback
#param 2 - appName - used to read [appName].fsg and [appName].db
recog = SpeakPythonRecognizer(execute, "megumi");

# sets the level of debug output
# 1 is the most output, 10 is the least
# default level is 3
recog.setDebug(1);

#call this to start recognizing speech
#I believe this call utilizes current thread. Please multi-thread it yourself if necessary.
stop = False
try:
	while not stop:
		recog.recognize();
except KeyboardInterrupt:
	stop = True;
	print "Interrupted.";
finally:
        time.sleep(0.00001)
