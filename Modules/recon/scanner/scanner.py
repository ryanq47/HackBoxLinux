import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)


print("""

a) Fast scan - Common Ports (1-1000)

b) Slow Scan - All Ports

---------------\n
h) Help
w) quit to MODE
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n
""")

statement=input().lower()


## Moving Around
if statement=="w":
	exec(open('HackBox.py').read()) 
if statement=="q":
	os.system('clear')
	exec(open('HackBox.py').read())   
	ans = None
# ------------ Mode Switch ----------------------#
if statement=="x":
	exec(open('Modules/attack/Attack.py').read()) 
if statement=="y":
	exec(open('Modules/defense/Defense.py').read()) 
if statement=="z":
	exec(open('Modules/recon/Recon.py').read()) 
## --






def scanner():
    #getting target
    print('Enter target IP:')
    target=input().lower()

        # No idea why this code is needed but it makes it work :)
    if len(sys.argv) == 2:
        
        # translate hostname to IPv4
        target = socket.gethostbyname(sys.argv[1])
    else:
        #print("No hostname found, proceeding with " + target + " as target")
        hostname = socket.gethostbyaddr(target)
        print("Hostname of target is {}".format(hostname))

    # Add Banner

    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    try:
        
        # will scan ports between 1 to 65,535
        for port in range(range2,range3):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                print("Port {} is open".format(port))
            s.close()
            
    except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
    except socket.error:
            print("\ Server not responding !!!!")
            sys.exit()





while True:
    if statement == 'a':
        range2=1
        range3=1000
        scanner()
    if statement == 'b':
        range2=1
        range3=65535
        scanner()

    else:
        print('No open ports found')
    statement=input().lower()




