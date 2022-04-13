#！/usr/bin/env python

## AutoTack - Auto scan and attack Module
## will eventually be integrated with a database (mariadb?) for storing scanned IP addresses 


## notes: db change: hackbox_db > 127.0.0.1 (or other IP) etc > each ip has a list of ports

## Dependencies: Nmap

import os
import mysql.connector
import subprocess as sp

## -- SQL connection -- ##
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="-Pokemon1"
  )
mycursor = mydb.cursor()
## -- -- ##
os.system('systemctl start mariadb')
os.system('clear')

print(r"""
  ___  _   _ _____ _____      _____ ___  _____  _   __
 / _ \| | | |_   _|  _  |    |_   _/ _ \/  __ \| | / /
/ /_\ \ | | | | | | | | |______| |/ /_\ \ /  \/| |/ / 
|  _  | | | | | | | | | |______| ||  _  | |    |    \ 
| | | | |_| | | | \ \_/ /      | || | | | \__/\| |\  \
\_| |_/\___/  \_/  \___/       \_/\_| |_/\____/\_| \_/
        """)

print("DevNote: The MariaDB formatting is a little wonky at the moment, will get fixed eventually ")

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
    ## reload statement/variable, needs to be at top so accessible to all further down
    if statment == 'reload':
        os.system('python3 /Modules/attack/AutoTack/autotack.py')
        reload = os.system('python3 /Modules/attack/AutoTack/autotack.py')

## --- interface --- ###
    elif statement =='a':
        targetIP = input('Enter target IP address:')
        #print(targetIP)
        nmapFLAGS = input('Enter additional NMAP flags - default are -sS and -Pn; syntax: "-a -T 4"')
        print("This may take a minute...")
        print("-----Open Ports-----")
        ## This code is running nmap scan, and saving it as the variable scanresult (need to import subprecess)
        ## note: stdout is piped through grep to filter by only numbers, then get rid of the "starting Nmap" message becuase it takes up alot of space
        scanresult = sp.getoutput('nmap ' + targetIP +' ' + nmapFLAGS + ' -Pn | grep -e "[0-9]*/" | grep -v "Starting"')
        ## for exluding everyhting but port numbers: |grep -o "[0-9]*"

        print(scanresult)
        ## convert '.' to '_' due to sql not accepting '.'
        convert = targetIP
        convert = convert.replace('.','_')
        targetIPinput = convert
        #targetipconvert = print(int(convert))



## --- Sql Interaction --- ##
        mycursor.execute("USE hackbox_ip_db")
        #mycursor.execute("INSERT INTO ip_addresses (ipaddress, port) VALUES (" + targetIP + "," + scanresult + ");")
        mycursor.execute("CREATE TABLE " + targetIPinput + " (OpenPorts text)")
        mycursor.execute("INSERT INTO " + targetIPinput + "(OpenPorts) VALUES ('" + scanresult+ "')")
        mydb.commit()
        print("----------")

    elif 'view ip' in statement:
        ipsummon = input()
        mycursor.execute("USE hackbox_ip_db")
        mycursor.execute("SELECT * FROM " + ipsummon)

        # This code below allows all data to be viewed in the db
        for x in mycursor:
            print (x)


    elif statement =='delete db':
        print("Are you sure you want to delete the DB? (y/N)")
        deletedb = input().lower()
        if 'y' in deletedb:
            mycursor.execute("DROP DATABASE hackbox_ip_db")
        elif 'n' in deletedb:
            reload
        else:
            reload
        #mycursor.execute("SHOW DATABASES")
        ## add a confirmation prompt here

        print('database hackbox_ip_db has been dropped')
        for x in mycursor:
            print (x)



    elif statement =='i':

        #Creating Database
        mycursor.execute("CREATE DATABASE hackbox_ip_db")
        mycursor.execute("USE hackbox_ip_db")
        # TEST TABLE #mycursor.execute("CREATE TABLE 127_0_0_1")#(ipaddress text, port text, time text )")
        #mycursor.execute("INSERT INTO ip_addresses (ipaddress, port) VALUES ('123.456.789.0', '69');")


        ## cleanup
        mydb.commit()
        ## these 2 are commented out becuase it closes cursor, which causes the need for a program restart. work on solution/notice later.
        #mydb.close()
        #mycursor.close()
        for x in mycursor:
            print (x)
        print('Database Created!')


    else:
        print('ya broke it doofus')
    statement = input("").lower()
