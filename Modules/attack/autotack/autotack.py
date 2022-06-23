#！/usr/bin/env python

## AutoTack - Auto scan and attack Module
## will eventually be integrated with a database (mariadb?) for storing scanned IP addresses 


## this script must be run as root!!
## notes: db change: hackbox_db > 127.0.0.1 (or other IP) etc > each ip has a list of ports

## Dependencies: Nmap

import os
#import mysql.connector
import bedb 
import subprocess as sp

## -- Defining Vars -- ##
DB_name = "hackbox_db"
TABLE_name = "hackbox_ip_table"


## -- global vars -- ##

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
    Note: Small issue with -Pn flag preventing it from being used 



---------------\n
h) Help
w) quit to MODE
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n

Type in IP address to view info:          """)
statement = input("").lower()

## --- Main Body Loop --- ##



while True:
    	## reload statement/variable, needs to be at top so accessible to all further down
	if statement == 'reload':
		os.system('clear')
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
        	
        	
		## yes this is jank... I had it written out for grep so it's gonna stay that way :)
		scanresult = sp.getoutput('nmap ' + targetIP +' ' + nmapFLAGS + ' | grep -e "[0-9]*/" | grep -v "Starting" |grep -o "[0-9]*"')
		
			# ideas:
			#scanresult = sp.getoutput('nmap ' + targetIP +' ' + nmapFLAGS + ' | grep -e "[0-9]*/" | grep -v "Starting" | tee Modules/attack/autotack/autotack_tmp/scan_tmp') # |grep -o "[0-9]*"') # --> issue with PN
			#scanresult_services = open("Modules/attack/autotack/autotack_tmp/scan_tmp", "r")
			
       		## for exluding everyhting but port numbers: |grep -o "[0-9]*"
		
			
		#print(scanresult_services.read())



		print('scanresult= ', scanresult)
		#print('scanresult_port = ', scanresult_ports)
		
		## bedb plugin
		#targetIP = ""
		#ports = ""
		services = ""
		
		data = {

            		'ip_addr' : targetIP,
            		'open_ports' : "",
            		'services' : ""
		}
		
		DB_name = "hackbox_db"
		TABLE_name = "hackbox_ip_table"
		COLUMN_name = targetIP
		
		bedb.writeCOLUMN(DB_name, TABLE_name, targetIP, data)
		bedb.readCOLUMN(DB_name,TABLE_name, targetIP, 'ip_addr')
		bedb.readCOLUMN(DB_name,TABLE_name, targetIP, 'open_ports')
		print(bedb.readCOLUMN.key_data) ## note! this is a variable under readCOLUMN, it does its own conversion from a Nonetype to a string, so if you need the string of an output, just use the .key_data
		attackList = bedb.readCOLUMN.key_data
		
		
		print("----------")

## -- Pulling from DB and scanning -- ##

        	# This pulls the port number from the db - in future will add service puller too (ex ssh)
		###attackList = sp.getoutput('cat /var/lib/mysql/hackbox_ip_db/tmp | grep -o "[0-9]"*')
		#print(attackList)

        	##print('Open Ports are:')
        	## this will output the ports stored. Now need to write AI/if commands for detecting ports
        	## ex: if 22 in tmp:
        	## then protocolcrack ssh or soemthing

## -- Final Confirmation & attack start -- ##
		print("Begin Attack? (y/N)")
		beginattack = input().lower()
		if 'y' in beginattack:
## Target Storage + Ip storage for modules
			targets = open("Modules/attack/autotack/autotack_exploits/targets_tmp", "w")
			#targets.write(attackList) #--> for troubleshooting, shows attackList
			targets.close

			targets = open("Modules/attack/autotack/autotack_exploits/targets_tmp", "r")
			print(targets.read())
			targets.close

			iptargets  = open("Modules/attack/autotack/autotack_exploits/iptargets_tmp", "w")
			iptargets.write(targetIP)
			iptargets.close

			iptargets  = open("Modules/attack/autotack/autotack_exploits/iptargets_tmp", "r")
			print(iptargets.read())
			iptargets.close
## -- Module Integration -- ## 
                	## I know this isn't very clean,but its all I got currently
			#print(attackList) --> troubleshoting to view attack list
			while True: ## eventually turn these into functions
				if '21' in attackList: # or '22' or '23' or '80' or '3389'
					os.system('python3 Modules/attack/autotack/exploits/bruteforce_hydra.py')
				elif '22' in attackList: # or '22' or '23' or '80' or '3389'
					os.system('python3 Modules/attack/autotack/exploits/bruteforce_hydra.py')
				elif '23' in attackList: # or '22' or '23' or '80' or '3389'
					os.system('python3 Modules/attack/autotack/exploits/bruteforce_hydra.py')
				elif '80' in attackList: # or '22' or '23' or '80' or '3389'
					os.system('python3 Modules/attack/autotack/exploits/bruteforce_hydra.py')
				elif '3389' in attackList: # or '22' or '23' or '80' or '3389'
					os.system('python3 Modules/attack/autotack/exploits/bruteforce_hydra.py')
				else:
					print("Target currently not attackable/not supported")
				break
				statement = input()
        		## Note: Need to find a way tomake it jump back to either autotack, or next script in line while stll pulling from
        		## the target_tmp file


## -- logging -- ##
            #logfile = open("logs/autotack.log", "a")
            #logfile.write(log)
            #logfile.close
## -- Y/n response -- ##
		elif 'n' in beginattack:
            		reload
		else:	
            		reload

## -- cleaning up -- ##
        #removing tmp file cause I dont know how to overwrite the file with mariadb yet :(
		os.system(" rm -rf /var/lib/mysql/hackbox_ip_db/tmp")
		
## -- DB IP lookup -- ##
	elif '.' in statement:
		targetIP = statement
		print('Open Ports:')
		bedb.readCOLUMN(DB_name,TABLE_name, targetIP, 'open_ports')
		print('Services:')
		bedb.readCOLUMN(DB_name,TABLE_name, targetIP, 'services')





        ## need to beable to put this ^^ in variable and then grep the output for only the numbers ports and type (tcp/udp) so that can be sent to a attack program
        #print(dbpull)
        # This code below allows all data to be viewed in the db

## -- Delete DataBase -- ##
	elif statement =='delete db':
		print("Are you sure you want to delete the DB? (y/N)")
		deletedb = input().lower()
		if 'y' in deletedb:
			mycursor.execute("DROP DATABASE hackbox_ip_db")
		elif 'n' in deletedb:
			reload
		else:
			reload

		print('database hackbox_ip_db has been dropped')
		for x in mycursor:
			print (x)


## -- Installing Database -- ##
	elif statement =='i':

        #Creating Database
			mycursor.execute("CREATE DATABASE hackbox_ip_db")
			mycursor.execute("USE hackbox_ip_db")
        # TEST TABLE #mycursor.execute("CREATE TABLE 127_0_0_1")#(ipaddress text, port text, time text )")
        #mycursor.execute("INSERT INTO ip_addresses (ipaddress, port) VALUES ('123.456.789.0', '69');")

			mydb.commit()
        ## these 2 are commented out becuase it closes cursor, which causes the need for a program restart. work on solution/notice later.
        #mydb.close()
        #mycursor.close()
			for x in mycursor:
				print (x)
			print('Database Created!')


# ----------- moving around ---------------------#
	elif statement=="h":
		print("""\nHelp
AutoTack! The crown jewels of HackBox!

AutoTack is an automatic scanner, logger, and attacker for  any target you select!	
First, It runs an NMAP scan, and saves those results to the SQL database
Then, it checks the NMAP results for any potential attack surface, and proceeds to attack from there. As of now, only bruteforce attacks are supported,
but more are incoming as I dive into  the world of exploits.

Bug Note: Currently, AutoTack has  an issue where it cannot pull a previously scanned IP and attack it - only view previous scan  results. TLDR It has to rescan the target each time

A potential  fix is to have 'attackList' be equal to the database output from previous scans, 

This will be solved in future releases, once I figure out how to have the database overwrite an entrty.
			""")
			### ^^ note: maybe have it drop the IP from the DB before rescanning, thus solving the multiple entry issues, however the 
			### Pulling and attacking from DB needs to be worked on
	elif statement=="w":
		exec(open('HackBox.py').read()) 
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


