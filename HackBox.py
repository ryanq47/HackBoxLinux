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
h)Help


              """)



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
    elif statement == ('new'):
        os.system('wt -w 0 nt')
    #Refresh/reload
    elif statement == 'refresh':
        os.system('clear')
        exec(open('HackBox.py').read()) 
    #BuildInfo
    elif statement == 'build':
        print (BUILD)
        print (QUESTION)

# -- Personal Tools -------------------------------------------------------------------
    #NetReport - A "quick" net report of IP addresses, Connected Ports, and __ all congregated in one spot

        #print('anything else I can do?')
    elif statement == ('netreport'):
        #import netreport
        subprocess.call('start python modules/netreport.py', shell=True)
        print('Generating Report in new window...')
        print('HackBox: Anything else I can do?')

    elif statement == ('scriptrunner -w'):
        subprocess.call('start python modules/programs/scriptrunner/scriptrunner.py', shell=True)
        print('Opening Scriptrunner in new window...')
        print('HackBox: Anything else I can do?')
    elif statement == ('scriptrunner'):
        exec(open('modules/programs/scriptrunner/scriptrunner.py').read()) 
        print('Opening Scriptrunner in new window...')
        print('HackBox: Anything else I can do?')

# --- programs -------------------------------------------------------------------- 
# --- tools not created by me, but useful for a variety of things ---
    elif statement == 'ipcam':
        #print('hi')
        exec(open('Modules/programs/surveillance/ipcam.py').read()) 
    elif statement == 'ipcam -w':
        #print('hi')
        subprocess.call('start python Modules/programs/surveillance/ipcam.py', shell=True)
        print('HackBox: Anything else I can do?')


    elif statement == 'usercheck':
        #print('hi')
        exec(open('Modules/programs/surveillance/usercheck.py').read()) 
    elif statement == 'usercheck -w':
        #print('hi')
        subprocess.call('start python Modules/programs/surveillance/usercheck.py', shell=True)
        print('HackBox: Anything else I can do?')



    elif statement == 'socialsearch':
        #print('hi')
        exec(open('Modules/programs/surveillance/socialsearch.py').read()) 
    elif statement == 'socialsearch -w':
        #print('hi')
        subprocess.call('start python Modules/programs/surveillance/socialsearch.py', shell=True)
        print('HackBox: Anything else I can do?')
        
    elif statement == 'keylogger':
        exec(open('Modules/programs/keylogger/keylogger.py').read()) 
    elif statement == 'keylogger -w':
        subprocess.call('start python Modules/programs/keylogger/keylogger.py', shell=True)
        print('HackBox: Anything else I can do?')
        
        #add email or file option, and a -f for fast start
# -- Modes ------------------------------------------------------------------
    elif statement == 'x':
        #print('hi')
        exec(open('Modules/attack/Attack.py').read())
    elif statement == 'y':
        #print('hi')
        exec(open('Modules/defense/Defense.py').read()) 
    elif statement == 'z':
        #print('hi')
        exec(open('Modules/recon/Recon.py').read()) 

#------------------------------------------------------------------------------
#Internet
#Search Feature: 
 
    elif 'search' in statement and statement != 'socialsearch':
        print('Searching The Internet for' , statement, "...")
        statement =statement.replace("search", "")
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(statement))

        print('HackBox: Anything else I can do?')

    elif 'google' in statement:
        print('Searching The Internet for' , statement, "...")
        statement =statement.replace("google", "")
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(statement))
 
        print('HackBox: Anything else I can do?')

    elif 'find' in statement:
        
        statement =statement.replace("find", "")
        print('Searching The Internet for' , statement, "...")
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(statement))

        print('HackBox: Anything else I can do?')

    elif 'summary' in statement:
        print('Searching The Internet...')
        statement =statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=2)
        print("---------------------------------------------------------------")
        print("According to the Internet:")
        print(results)  
        print("---------------------------------------------------------------")
        print('HackBox: Anything else I can do?')

        # direct website connect
    elif '.com' in statement:
	
        webbrowser.open_new_tab('https://{}'.format(statement))
        print("Going to", statement)
        print("Anything else I can do for you?")

    elif '.org' in statement:
	    
        webbrowser.open_new_tab('https://{}'.format(statement))
        
        print("Going to", statement)
        print("Anything else I can do for you?")

    elif '.edu' in statement:
	    
        webbrowser.open_new_tab('https://{}'.format(statement))
        print("Going to", statement)
        print("Anything else I can do for you?")

    elif '.gov' in statement:
	
        webbrowser.open_new_tab('https://{}'.format(statement))
        print("Going to", statement)
        print("Anything else I can do for you?")

    #This is a loop that allows for any value in CMD to be checked, and run MUST GO LAST
    elif any((c in NETWORK) for c in NETWORK):
        print('---------------------------------------------------')
        os.system(statement)
        print('---------------------------------------------------')
        print("Anything else I can do for you?")
#------------------------------------------------------------------------------
    else:
        print('invalid command - type new for standard shell')
    statement = input("").lower()



os.system('pause')


