#!/usr/bin/env python3
#hackboxlinux attack mode
## use argparse or click for arguments
import os
import argparse
from xml.etree.ElementTree import TreeBuilder

#Variables



#clears screen to clean things up
os.system('clear')

print(r"""
  ___ _____ _____ ___  _____  _   __  ___  ______________ _____ 
 / _ \_   _|_   _/ _ \/  __ \| | / /  |  \/  |  _  |  _  \  ___|
/ /_\ \| |   | |/ /_\ \ /  \/| |/ /   | .  . | | | | | | | |__  
|  _  || |   | ||  _  | |    |    \   | |\/| | | | | | | |  __| 
| | | || |   | || | | | \__/\| |\  \  | |  | \ \_/ / |/ /| |___ 
\_| |_/\_/   \_/\_| |_/\____/\_| \_/  \_|  |_/\___/|___/ \____/ 
                                                                
                    """)
                    
print("Recon mode activated, type help for help")

print("""
OPTIONS 
a) System Access - Password Cracking, Backdoors, and more #(DELME; passwd dumper? - netcat backdoor for sure)
b) Denial Of Service

s) Scriptrunner - Offensive scripts
---
h)Help
q)Exit/Quit
---
x)Attack Mode
y)Defense Mode
z)Recon Mode
              """)

statement = input("").lower()
# ----------- Main Menu ---------------------#
while True:
# ----------- System Access ---------------------#
       if statement=="a":
              os.system('clear')
              print("\nSystem Access:")
              while True:   
                     
                     print("""

a)Protocol Cracker
b)Netcat Backdoor - In Progress
c)*Coming Soon* ( HashCat? - set up similar to protocl cracker?)
d)*Coming Soon*
---------------

q) quit

                                   """)
                     statement2 = input("").lower()
                     if statement2=="a":
                            os.system('clear')
                            exec(open('Modules/attack/systemaccess/protocolcracker/protocolcracker.py').read()) 

                     elif statement2=="b":
                            os.system('clear')
                            exec(open('modules/').read())   

                     elif statement2=="c":
                            os.system('clear')
                            exec(open('modules/').read()) 

                     elif statement2=="d":
                            os.system('clear')
                            exec(open('Modules/').read())  
                            ans = None
                     elif statement2=="q":
                            os.system('clear')
                            exec(open('Modules/attack/Attack.py').read())
                     else:
                            print("\n Not Valid Choice Try again")
                     statement2 = input("").lower()
# ----------- Denial Of Service ---------------------#
       elif statement=="b":
              os.system("clear")
              print("Denial Of Service:")
       elif statement=="s":
              os.system("clear")
              exec(open('Modules/attack/scriptrunner/scriptrunner.py').read()) 

# ----------- moving around ---------------------#
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