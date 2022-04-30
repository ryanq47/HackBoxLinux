import os
import webbrowser
import sys
print(r"""
 _   _ _____ ___________   _____  _   _  _____ _____  _   __   
| | | /  ___|  ___| ___ \ /  __ \| | | ||  ___/  __ \| | / /  
| | | \ `--.| |__ | |_/ / | /  \/| |_| || |__ | /  \/| |/ /   
| | | |`--. \  __||    /  | |    |  _  ||  __|| |    |    \    
| |_| /\__/ / |___| |\ \  | \__/\| | | || |___| \__/\| |\  \  
 \___/\____/\____/\_| \_|  \____/\_| |_/\____/ \____/\_| \_/
            """)

print('USERCHECK! Find where a username is being used! Type help for help, or type in a username!')
print('Example: check JohnDoe195')

print("""
---------------\n
h) Help
w) quit to Recon Mode
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n

Enter a username, or option:""")

statement = input("").lower()

while True:
	if 'check' in statement:
		print('USERCHECK: Checking common sites for users...')
		statement =statement.replace("check ", "")
		webbrowser.open_new_tab('https://knowem.com/checkusernames.php?u={}'.format(statement))
		print("USERCHECK: Anyone else you wanna spy on?")

	elif 'help' in statement:
		print("-----------------------------------------------------------------")
		print(" --- General Config ---")
		print("'check USERNAME': Searches most common sites for usernames in use")
		print("EX: check bobbert123")
		print('')
		print("'exit': Exits back to HackBox")
        #print("'NOT: enter 'socialsearch' to enter socialsearch at any time!")
		print("-----------------------------------------------------------------")

		print("USERCHECK: Anyone else you wanna spy on?")

    #elif statement == 'socialsearch':   
        #print('USERCHECK: Opening SocialSearch')
        #exec(open('socialsearch.py').read()) 

# ----------- moving around ---------------------#
	elif statement=="h":
		print("\nHelp")
	elif statement=="w":
		exec(open('Modules/recon/Recon.py').read()) 
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







    ## maybe make this pop out on its own window - OR create a settings page taht the user can edit