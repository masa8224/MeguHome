#SpeakPython allows developers to add speech recognition support to their Python applications
#Copyright (C) 2015  Eric Matthews

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by 
#the Free Software Foundation, either version 3 of the License, or 
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of 
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os;
import sys;

def printHelp():
	print "\nRun this module by typing:\n\n\tpython MakeProject.py [appName] [sps file/folder]\n\n\tExample: python MakeProject.py calc calc.sps\n\n";

if len(sys.argv) < 3:
	print "Invalid command.";
	printHelp();
	sys.exit();

appName = sys.argv[1];
spsName = sys.argv[2];

#make database files
print "Trying to create database (" + appName  + ".db) from sps files...";
os.system("python SpeakPythonMakeDB.py " + appName + " " + spsName);


print "Trying to create jsgf grammar used for speech recognition from sps files...";
retCode = os.system("python SpeakPython/SpeakPythonMakeJSGF.py " + appName + " " + appName + ".sps");

#do only if JSGF parse succeeded
if retCode == 0:
    print "Trying to convert jsgf grammar into an fsg grammar using sphinx_jsgf2fsg for use with pocketsphinx speech recognition...";
    os.system("sphinx_jsgf2fsg -jsgf " + appName + ".jsgf -fsg " + appName + ".fsg");
