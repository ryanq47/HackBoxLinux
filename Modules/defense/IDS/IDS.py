#!/usr/bin/env python3
#IDS

#maybe make a class out of this? - might save some code


# now a logger to see if anyone is in the system

# Note: not picking up ssh login attempts... hmmm

import os
import subprocess as sp
import time

os.system('clear')



print("""
        _____      _                  _              ______     _            _   _               _____           _                 
       |_   _|    | |                (_)             |  _  \   | |          | | (_)             /  ___|         | |                
         | | _ __ | |_ _ __ _   _ ___ _  ___  _ __   | | | |___| |_ ___  ___| |_ _  ___  _ __   \ `--. _   _ ___| |_ ___ _ __ ___  
         | || '_ \| __| '__| | | / __| |/ _ \| '_ \  | | | / _ \ __/ _ \/ __| __| |/ _ \| '_ \   `--. \ | | / __| __/ _ \ '_ ` _ \ 
        _| || | | | |_| |  | |_| \__ \ | (_) | | | | | |/ /  __/ ||  __/ (__| |_| | (_) | | | | /\__/ / |_| \__ \ ||  __/ | | | | |
        \___/_| |_|\__|_|   \__,_|___/_|\___/|_| |_| |___/ \___|\__\___|\___|\__|_|\___/|_| |_| \____/ \__, |___/\__\___|_| |_| |_|
                                                                                                        __/ |                      
                                                                                                        |___/                       
                                                                                                        """)
print("A basic IDS - meant to show incoming connections, and log them. Will add firewall options to block later!")
print("Type help for help")

print("""
OPTIONS 
a)Start
b)SOMETHING
---
h)Help
4)Back
q)Exit/Quit
            """)


while True:
    statement = input("").lower()
    #IDS logic ----------------------------------------------------------------------------------
    if statement == "a":
        #os.system('clear')
        while True:
            print('Time               Outside IP           Inside IP            protocol')
            os.system("sudo tcpdump -nn  | tee -a connectionlog.txt" )
            os.system("echo ---------- >> connectionlog.txt ")
            time.sleep(5)
    #--------------------------------------------------------------------------------------------
    
    elif statement == 'h':
        print("-----------------------------------------------------------------")
        print(" --- General Config ---")
        print(" 'Start': Starts the monitoring")
        print(" 'Exit': Exits to Defensive mode")
        print("-----------------------------------------------------------------")



    elif statement == 'exit' or statement == 'q':
        exec(open('Modules/defense/Defense.py').read()) 

#timer function! works :)
#while True:
    #print('hello timer')
    #time.sleep(10)
