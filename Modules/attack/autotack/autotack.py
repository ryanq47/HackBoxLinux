#！/usr/bin/env python

## AutoTack - Auto scan and attack Module
## will eventually be integrated with a database (mariadb?) for storing scanned IP addresses 

## Dependencies: Nmap

import os


os.system('clear')

print(r"""
  ___  _   _ _____ _____      _____ ___  _____  _   __
 / _ \| | | |_   _|  _  |    |_   _/ _ \/  __ \| | / /
/ /_\ \ | | | | | | | | |______| |/ /_\ \ /  \/| |/ / 
|  _  | | | | | | | | | |______| ||  _  | |    |    \ 
| | | | |_| | | | \ \_/ /      | || | | | \__/\| |\  \
\_| |_/\___/  \_/  \___/       \_/\_| |_/\____/\_| \_/
        """)

## --- Menu --- ###
print("""
OPTIONS 
a) Scan and Can (Nmap + Common Password Bruteforce)
b) ???
---
h)Help
q)Exit/Quit
---
              """)


statement = input("").lower()

## --- Main Body Loop --- ##
while True:
    if statement =='a':
        targetIP = input('Enter target IP address:')
        #print(targetIP)
        nmapFLAGS = input('Enter additional NMAP flags - default are -sS and -Pn; syntax: "-a -T 4"')
        print("----------")
        os.system('nmap ' + targetIP + nmapFLAGS + ' -sS -Pn  |tee -a db/scannedIPs/' + targetIP + '.db') ##Store result in database - this is a temporary solution
        #os.system('echo stdout | grep / >> db.txt')
        print("----------")
        #print(__file__)
        #os.system('pwd')





    