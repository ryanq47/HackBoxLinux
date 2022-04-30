#Version 1.1 4/29/22

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
                    
print("Attack mode activated!")

print("""
OPTIONS\n
a) System Access - Password Cracking, Backdoors, and more 
b) Denial Of Service\n
---------------\n
h) Help
q) Exit/Quit\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n
Enter an option:              """)

statement = input("").lower()

while True:

# ----------- System Access ---------------------#
	if statement=="a":
		os.system('clear')
		print(r"""
 _____              _                      ___                            
/  ___|            | |                    / _ \                           
\ `--.  _   _  ___ | |_  ___  _ __ ___   / /_\ \  ___  ___  ___  ___  ___ 
 `--. \| | | |/ __|| __|/ _ \| '_ ` _ \  |  _  | / __|/ __|/ _ \/ __|/ __|
/\__/ /| |_| |\__ \| |_|  __/| | | | | | | | | || (__| (__|  __/\__ \\__ \
\____/  \__, ||___/ \__|\___||_| |_| |_| \_| |_/ \___|\___|\___||___/|___/
         __/ |                                                            
        |___/  
              """)
              
		print("""

a) Protocol Cracker (Login Bruteforcing)
b) Eternal Blue
c) AutoTack\n
---------------\n
h) Help
w) quit to Attack Mode
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n

Enter an option:			""")
		while True:  
			statement2 = input("").lower()


			if statement2=="a":
				os.system('clear')
				exec(open('Modules/attack/systemaccess/protocolcracker/protocolcracker.py').read()) 
			elif statement2=="b":
				os.system('clear')
				exec(open('Modules/attack/systemaccess/eternalblue/module_eternalblue.py').read())

			elif statement2=="c":
				os.system('clear')
				exec(open('Modules/attack/autotack/autotack.py').read())  
				ans = None
			elif statement2=="q":
				os.system('clear')
				exec(open('Modules/attack/Attack.py').read())

		# ----------- moving around ---------------------#
			elif statement2=="h":
				print("\nHelp")
			elif statement2=="w":
				exec(open('Modules/attack/Attack.py').read()) 
				ans = None
			elif statement2=="q":
				os.system('clear')
				exec(open('HackBox.py').read())   
				ans = None
		# ------------ Mode Switch ----------------------#
			elif statement2=="x":
				exec(open('Modules/attack/Attack.py').read()) 
			elif statement2=="y":
				exec(open('Modules/defense/Defense.py').read()) 
			elif statement2=="z":
				exec(open('Modules/recon/Recon.py').read()) 
			else:
				print("\nOption not found, type help for help")
			statement2 = input("").lower()

# ----------- Denial Of Service ---------------------#
	if statement=="b":
		os.system('clear')
		print(r"""
______              _         _   _____   __   _____                     _            
|  _  \            (_)       | | |  _  | / _| /  ___|                   (_)           
| | | | ___  _ __   _   __ _ | | | | | || |_  \ `--.   ___  _ __ __   __ _   ___  ___ 
| | | |/ _ \| '_ \ | | / _` || | | | | ||  _|  `--. \ / _ \| '__|\ \ / /| | / __|/ _ \
| |/ /|  __/| | | || || (_| || | \ \_/ /| |   /\__/ /|  __/| |    \ V / | || (__|  __/
|___/  \___||_| |_||_| \__,_||_|  \___/ |_|   \____/  \___||_|     \_/  |_| \___|\___|
              """)
		while True:   
                     
			print("""

a) MITM Arp Spoof

---------------\n
h) Help
w) quit to MODE
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n


Enter an option:                                   """)
			statement2 = input("").lower()
			if statement2=="a":
				os.system('clear')
				exec(open('Modules/attack/DOS/arpspoof.py').read()) 

			elif statement2=="b":
				os.system('clear')
				exec(open('Modules/attack/DOS/').read())   

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

		# ----------- moving around ---------------------#
			elif statement2=="h":
				print("\nHelp")
			elif statement2=="w":
				exec(open('Modules/attack/Attack.py').read()) 
				ans = None
			elif statement2=="q":
				os.system('clear')
				exec(open('HackBox.py').read())   
				ans = None
		# ------------ Mode Switch ----------------------#
			elif statement2=="x":
				exec(open('Modules/attack/Attack.py').read()) 
			elif statement2=="y":
				exec(open('Modules/defense/Defense.py').read()) 
			elif statement2=="z":
				exec(open('Modules/recon/Recon.py').read()) 
			else:
				print("\nOption not found, type help for help")
			statement2 = input("").lower()


# ----------- moving around ---------------------#
	elif statement=="h":
		print("""\n
Welcome the HackBox Attack Mode front page, this is where you can access every attack tool HackBox contains.

System Access contains tools for gaining initial access to a system. 

Denial Of service contains tools to shut down, or deny access to services
			""")

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

#os.system('pause')
