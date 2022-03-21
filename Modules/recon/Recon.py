#!/usr/bin/env python3
#hackboxlinux defense mode
## use argparse or click for arguments
import os
import argparse
from xml.etree.ElementTree import TreeBuilder

#Variables



#clears screen to clean things up
os.system('clear')

print(r"""
______ _____ _____ _____ _   _  ___  ______________ _____ 
| ___ \  ___/  __ \  _  | \ | | |  \/  |  _  |  _  \  ___|
| |_/ / |__ | /  \/ | | |  \| | | .  . | | | | | | | |__  
|    /|  __|| |   | | | | . ` | | |\/| | | | | | | |  __| 
| |\ \| |___| \__/\ \_/ / |\  | | |  | \ \_/ / |/ /| |___ 
\_| \_\____/ \____/\___/\_| \_/ \_|  |_/\___/|___/ \____/ 
                                                          
                    """)
                    
print("Recon mode activated, type help for help")

print("""
OPTIONS 
a)Surveillance
b)Keylogger
---
h)Help
q)Exit/Quit
---
x)Attack Mode
y)Defense Mode
z)Recon Mode
              """)

statement = input("").lower()

while True:
       #os.system('clear')
              #ans=raw_input
       #ans=raw_input("What would you like to do? ")
       if statement=="a":
              print("\nSurveillance options:")
              while True:   
                     
                     print("""

a)IP-CAM
b)SocialSearch
c)UserCheck
d)Back


                                   """)
                     statement2 = input("").lower()
                     if statement2=="a":
                            exec(open('modules/recon/surveillance/ipcam.py').read())            
                     elif statement2=="b":
                            exec(open('modules/recon/surveillance/socialsearch.py').read())   
                     elif statement2=="c":
                            exec(open('modules/recon/surveillance/usercheck.py').read())   
                     elif statement2=="d":
                            exec(open('Modules/recon/Recon.py').read())  
                            ans = None
                     else:
                            print("\n Not Valid Choice Try again")
                     statement2 = input("").lower()

       elif statement=="b":
              print("\nKeylogger")
# ------------ Movement----------------------#
       elif statement=="c":
              print("\nHelp")
       elif statement=="h":
              print("\n Goodbye") 
              ans = None
       elif statement=="q":
              os.system('clear')
              exec(open('HackBox.py').read())   
              ans = None
# ------------ Mode Switch ----------------------#
       elif statement=="x":
            exec(open('Modules/attack/Attack.py').read()) 
       elif statement=="y":
            exec(open('Modules/defense/Defense.py').read()) 
       elif statement=="z":
            exec(open('Modules/recon/Recon.py').read()) 
       else:
              print("\nOption not found, type help for help")
       statement = input("").lower()

os.system('pause')