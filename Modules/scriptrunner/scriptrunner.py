import datetime
#import wikipedia
#import webbrowser
#import pynput.keyboard 
import os
#import sys
#import signal
import time
import subprocess
#import wolframalpha
import json
import requests
#import glob

#file imports
os.system('clear')
print(r"""
 _____ _____ ______ ___________ ___________ _   _ _   _  _   _  ___________    __        _____ 
/  ___/  __ \| ___ \_   _| ___ \_   _| ___ \ | | | \ | || \ | ||  ___| ___ \  /  |      |  _  |
\ `--.| /  \/| |_/ / | | | |_/ / | | | |_/ / | | |  \| ||  \| || |__ | |_/ /  `| |      | |/' |
 `--. \ |    |    /  | | |  __/  | | |    /| | | | . ` || . ` ||  __||    /    | |      |  /| |
/\__/ / \__/\| |\ \ _| |_| |     | | | |\ \| |_| | |\  || |\  || |___| |\ \   _| |_  _  \ |_/ /
\____/ \____/\_| \_|\___/\_|     \_/ \_| \_|\___/\_| \_/\_| \_/\____/\_| \_|  \___/ (_)  \___/ 
                                                                                               
                                                                                               
                                                                                              
                                                                                              
                                                                            
                                                                            
""")
print('SCRIPTRUNNER! (1.0) An easy script running tool! Type help for help, or a script name to run it! EX: "test.bat" - No ./ required!')
print('Current Available Scripts: ')



# ------ script sorter ------- #

print('### --- Shell Files: --- ###')
os.system('ls Modules/scriptrunner/scripts/ | grep .sh')

print('--')

print('### --- Python Files: --- ###')
os.system('ls Modules/scriptrunner/scripts/ | grep .py')
print('--')

print('### --- Local Reverse Shells: --- ###')
os.system('ls Modules/scriptrunner/scripts/ | grep _rev')
print('--')

print('SCRIPTRUNNER: What should I run?')
statement = input("").lower()

## make it autodisplay availabel scripts in directory
# ------ While True Loop ------- #

while True:
    if '.py' in statement:
        print("")
        print('running', statement)
        pyscript = "python3 Modules/scriptrunner/scripts/{0}".format(statement)
        os.system(pyscript)
        print("")
        print('SCRIPTRUNNER: What should I run?')

    # -- Shell --
    elif '.sh' in statement:
        print("")
        print('running', statement)

        os.system('bash Modules/scriptrunner/scripts/'+statement)
        print("")
    elif '_rev' in statement:
        print("")
        print('running', statement)

        os.system('bash Modules/scriptrunner/scripts/'+statement)
        print("")

        #os.system('./Modules/scriptrunner/scripts/pingsweep.sh')
## notes: to run a .sh using os.system, define a variable (cmd) then insert command and add {0} for the variable
## {1}, {2}... for more variables. then add .format(var) so it knows those are variables



    elif 'help' in statement:
        print("-----------------------------------------------------------------")
        print(" --- General Config ---")
        print('')
        print("'SCRIPTNAME.FILETYPE': Runs script if found in script folder")
        print(" EX: 'test.sh")
        print('')
        print(" --- Permissions ---")
        print('')
        print(" Allowing a script to be run:")
        print(" chmod +x SCRIPTNAME.sh ")
        print('')
        print(" Running said script:")
        print(" ./SCRIPTNAME.sh ")
        print("-----------------------------------------------------------------")

        print("SCRIPTRUNNER: Anything I can do for you?")
    elif statement == 'exit':
        print('SCRIPTRUNNERI: Exiting SCRIPTRUNNER')

        #This is a loop that allows for any value in CMD to be checked, and run MUST GO LAST
    elif any((c in NETWORK) for c in NETWORK):
        print('---------------------------------------------------')
        os.system(statement)
        print('---------------------------------------------------')
        print("Anything else I can do for you?")

    else:
        print('SCRIPTRUNNER: Invalid Paramater, type help for help, or exit to exit')

    statement = input("").lower()




  
