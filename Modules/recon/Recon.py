# ReconMode ver 1.1 4/30/22
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
a) Surveillance


---------------\n
h) Help
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n

Enter an option:  """)
# add keylogger in  eventually

statement = input("").lower()

while True:
       #os.system('clear')
              #ans=raw_input
       #ans=raw_input("What would you like to do? ")
	if statement=="a":
		os.system('clear')
		print("""\n

 _____ _   _______ _   _ _____ _____ _      _       ___   _   _ _____  _____ 
/  ___| | | | ___ \ | | |  ___|_   _| |    | |     / _ \ | \ | /  __ \|  ___|
\ `--.| | | | |_/ / | | | |__   | | | |    | |    / /_\ \|  \| | /  \/| |__  
 `--. \ | | |    /| | | |  __|  | | | |    | |    |  _  || . ` | |    |  __| 
/\__/ / |_| | |\  \ \_/ / |___ _| |_| |____| |____| | | || |\  | \__/\| |___ 
\____/ \___/\_| \_|\___/\____/ \___/\_____/\_____/\_| |_/\_| \_/\____/\____/ 
                                                                            
		""")
		while True:   
                     
			print("""

a) IP-CAM
b) UserCheck\n
---------------\n
h) Help
w) quit to Survelliance
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n
Enter Option:                                   """)
			statement2 = input("").lower()
			if statement2=="a":
				os.system('clear')
				exec(open('Modules/recon/surveillance/ipcam.py').read())            
                     #elif statement2=="b":
                            #exec(open('modules/recon/surveillance/socialsearch.py').read())   
			elif statement2=="b":
				os.system('clear')
				exec(open('Modules/recon/surveillance/usercheck.py').read())   
			elif statement2=="c":
				os.system('clear')
				exec(open('###').read())  
				ans = None
			# ----------- moving around ---------------------#
			elif statement2=="h":
				print("\nHelp")
			elif statement2=="w":
				exec(open('Modules/recon/Recon.py').read()) 
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

			

	elif statement=="b":
		print("\nKeylogger")


# ----------- moving around ---------------------#
	elif statement=="h":
		print("\nHelp")
	elif statement=="w":
		exec(open('Modules/recon/Recon.py').read()) 
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