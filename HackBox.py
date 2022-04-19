#!/usr/bin/env python3
#V 1.1 - HACKBOXLINUX by Ryan Kleffman 
#2/7/2022

#changes---------------------------------------------------------
#edited refresh to clear screen on linux
#Added Tux splash (linux penguin)

#TO add:
# Defense mode, has clam av, rkhunter, fail2ban and lots of logging

# NEed to add a map for visuals showing hackbox, then its respective modes, ( lieka  network map)
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
BUILD = ["HackBoxLinux: Version 1.1; 2/7/2022; ryanq47"]
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
OPTIONS 
x)Attack Mode
y)Defense Mode
z)Recon Mode
s)Scriptrunner
h)Help


If connecting through netcat, type any command below to run on local system:          """)



statement = input("").lower()
while True:
#Intro
    if statement == ("hi"):
	    print ("Hackbox: Hello"); print("Hackbox: Anything else I can do?")

    elif statement == ("h") or statement == "help":
        print("-----------------------------------------------------------------")
        print(" --- General Config ---")
        #print("'new'                           : Opens a Blank Empty shell in new window")
        print("'refresh'                       : Reloads Hackbox") 
        print("'Search', 'Google', or 'Find'   : Find Relevant info in less clicks - works just like a search bar")
        print("'Summary'                       : Gives wikipedia summary, sometimes crashes so proceed at your own risk")
        print("'SITENAME'.com - ex; reddit.com : Type this in wherever, and it'll open said site,")
        print("                                : make sure to include .com, or .edu, etc!")
        print("-----------------------------------------------------------------")
        print(" --- Custom Tools/Modules --- ")
        # move to recon mode - but put script runner in here, and maybe offensive, and defensive with scripts for each respective style
        print("NETREPORT    : A 'quick' net report of IP addresses, and connected ports to give an overview of your system's connections!")
        print("SCRIPTRUNNER    : A built in easy script execution shell, just pop your script in the scripts folder!")       
        print(" --- External Tools/Modules --- ")
        print("IPCAM        : A free database of publicly accessible cameras all over the world")
        print("USERCHECK    : See if a username is being used anywhere!")
        print("SOCIALSEARCH : Open a direct FB, Insta, and Linkedin Page with just a (valid) username!")
        #print("KEYLOGGER    : A Keylogger that records to a file, or sends to your email - use at your own discretion")
        print("-----------------------------------------------------------------")
        # get argparse working and able to do stuff like hackbox.py -d etc
        print(" Modes          Command to Enter mode") 
        print("Defensive Mode (defense, -d) : Hackbox in full defensive mode, great for Blue team ")
        print("Attack Mode    (attack, -a): Hackbox in full offensive mode, Great for Red team ")
        print("Recon Mode     (recon, -r): Hackbox in Recon, or spy mode - Great for gathering info ")
        print("-----------------------------------------------------------------")
        #print(" --- Arguments ---")
        #print("-----------------------------------------------------------------")
        print("Note:")
        print("-  Case does not matter - upper and lower work the same")
        print("-  Any standard bash commands should work within Hackbox, just type it in - though you may need sudo")
        print(".................................................................")
        print("HackBox: Anything I can do for you?")


# -- passthrough commands
#Connection Shiz


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


