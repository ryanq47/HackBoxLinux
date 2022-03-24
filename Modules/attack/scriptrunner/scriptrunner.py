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
print(r"""
 _____ _____ ______ ___________ ___________ _   _ _   _  _   _  ___________    __        _____ 
/  ___/  __ \| ___ \_   _| ___ \_   _| ___ \ | | | \ | || \ | ||  ___| ___ \  /  |      |  _  |
\ `--.| /  \/| |_/ / | | | |_/ / | | | |_/ / | | |  \| ||  \| || |__ | |_/ /  `| |      | |/' |
 `--. \ |    |    /  | | |  __/  | | |    /| | | | . ` || . ` ||  __||    /    | |      |  /| |
/\__/ / \__/\| |\ \ _| |_| |     | | | |\ \| |_| | |\  || |\  || |___| |\ \   _| |_  _  \ |_/ /
\____/ \____/\_| \_|\___/\_|     \_/ \_| \_|\___/\_| \_/\_| \_/\____/\_| \_|  \___/ (_)  \___/ 
                                                                                               
                                                                                               
                                                                                              
                                                                                              
                                                                            
                                                                            
""")
print('SCRIPTRUNNER! (1.0) An easy script running tool! Type help for help, or a script name to run it! EX: test.bat')
print('Current Available Scripts: ')



# ------ script sorter ------- #
print('--')
print('Shell Files:')
os.system('ls Modules/attack/scriptrunner/scripts/ | grep .sh')

print('--')

print('Python Files:')
os.system('ls Modules/attack/scriptrunner/scripts/ | grep .py')
print('--')

print('SCRIPTRUNNER: What should I run?')
statement = input("").lower()

## make it autodisplay availabel scripts in directory
# ------ While True Loop ------- #

while True:
    if '.py' in statement:
        print('running', statement)
        pyscript = "python3 Modules/attack/scriptrunner/scripts/{0}".format(statement)
        os.system(pyscript)
        print('SCRIPTRUNNER: What should I run?')

    # -- Shell --
    elif '.sh' in statement:
        print('running', statement)
        shscript = "Modules/attack/scriptrunner/scripts/{0}".format(statement)
        os.system(shscript)

## notes: to run a .sh using os.system, define a variable (cmd) then insert command and add {0} for the variable
## {1}, {2}... for more variables. then add .format(var) so it knows those are variables



    elif 'help' in statement:
        print("-----------------------------------------------------------------")
        print(" --- General Config ---")
        print('')
        print("'SCRIPTNAME.FILETYPE': Runs script if found in script folder")
        print(" EX: 'test.bat")
        print('')
        print(" --- Permissions ---")
        print('')
        print(" --- useful for if you have Poweshell script execution disabled")
        print("'ps policy bypass'                       : Allows ALL PS scripts to be run on local user - Potentially dangerous!!")
        print('')
        print("'ps policy all'                       : Allows all SIGNED PS scripts to be run on local user")
        print('')
        print("'ps policy restricted'                        : restricts PS scripts from being run ")
        print('')
        print("'ps policy default'                  : Sets default settings for PS scripts, may lead to different results based") 
        print("                                       on Domain settings")
        print("-----------------------------------------------------------------")

        print("SCRIPTRUNNER: Anything I can do for you?")
    elif statement == 'exit':
        print('SCRIPTRUNNERI: Exiting SCRIPTRUNNER')
        
        exec(open('HackBox.py').read()) 
    else:
        print('SCRIPTRUNNER: Invalid Paramater, type help for help, or exit to exit')

    statement = input("").lower()




  