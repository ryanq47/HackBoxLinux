#！/usr/bin/env python

## AutoTack - Auto scan and attack Module
## will eventually be integrated with a database (mariadb?) for storing scanned IP addresses 

## Dependencies: Nmap

import os
import mysql.connector
## -- SQL connection -- ##
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="-Pokemon1"
  )
mycursor = mydb.cursor()
## -- -- ##
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


i) Install: Run First time only! This creates the database
    Note: type 'delete db' to drop the DB
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
    elif statement =='delete db':
        mycursor.execute("DROP DATABASE hackbox_db")
        #mycursor.execute("SHOW DATABASES")
        ## add a confirmation prompt here
        print('database hackbox_db has been dropped')
        for x in mycursor:
            print (x)



    elif statement =='i':

        #Creating Database
        mycursor.execute("CREATE DATABASE hackbox_db")
        mycursor.execute("USE hackbox_db")
        mycursor.execute("CREATE TABLE ip_addresses (ipaddress text, port text, time text )")
        mycursor.execute("INSERT INTO ip_addresses (ipaddress, port) VALUES ('123.456.789.0', '69');")


        ## cleanup
        mydb.commit()
        mydb.close()
        mycursor.close()
        for x in mycursor:
            print (x)
        print('Database Created!')
    else:
        print('ya broke it doofus')
    statement = input("").lower()