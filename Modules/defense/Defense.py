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

** coming in future updates! **
For now, check out scriptrunner for defensive scripts

---------------\n
h) Help

q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n

Enter an option:
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

# ----------- moving around ---------------------#
	elif statement=="h":
		print("\nHelp")
	elif statement=="w":
		exec(open('HackBox.py').read()) 
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