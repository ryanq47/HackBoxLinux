#!/usr/bin/env python3
#hackboxlinux defense mode
## use argparse or click for arguments
import os
import argparse

#Variables



#clears screen to clean things up
os.system('clear')

print(r"""
______ ___________ _____ _   _  _____ _____  ___  ______________ _____ 
|  _  \  ___|  ___|  ___| \ | |/  ___|  ___| |  \/  |  _  |  _  \  ___|
| | | | |__ | |_  | |__ |  \| |\ `--.| |__   | .  . | | | | | | | |__  
| | | |  __||  _| |  __|| . ` | `--. \  __|  | |\/| | | | | | | |  __| 
| |/ /| |___| |   | |___| |\  |/\__/ / |___  | |  | \ \_/ / |/ /| |___ 
|___/ \____/\_|   \____/\_| \_/\____/\____/  \_|  |_/\___/|___/ \____/ 
                                                                      
                    """)
                    
print("Defense mode activated, type help for help")

print("""
OPTIONS 
a)Intrusion Detection System
b)SOMETHING

s) Scriptrunner - Defensive Scripts
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
              exec(open('Modules/defense/IDS/IDS.py').read()) 

       elif statement=="b":
              print("\n - -")
       elif statement=="s":
              os.system('clear')
              exec(open('Modules/defense/scriptrunner/scriptrunner.py').read()) 
#-------------Movement -------------------------#
       elif statement=="h":
              print("\nHelp")

       elif statement=="d":
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