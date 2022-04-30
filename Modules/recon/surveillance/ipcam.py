#ReconMode ver 1.1 4/30/22
import webbrowser
print(r"""
 ___________   _____   ___  ___  ___   
|_   _| ___ \ /  __ \ / _ \ |  \/  |  
  | | | |_/ / | /  \// /_\ \| .  . |  
  | | |  __/  | |    |  _  || |\/| |   
 _| |_| |     | \__/\| | | || |  | |  
 \___/\_|      \____/\_| |_/\_|  |_/  
                                                    
                """)

print('IPCAM! Find Publicly available cameras on the internet! Type Help For help!')
print('Search Options: Country (Alpha-2 codes, ex AU for Australia), Place, City, Cameratype')
print('Syntax: "SearchOption" "Location/country" - ex "Country AU", or "City Dallas"\n')


print("""
---------------\n
h) Help
w) quit to Recon Mode
q) Exit to HackBox\n
---------------\n
x) Attack Mode
y) Defense Mode
z) Recon Mode\n

Enter where you want to search:

		""")

statement = input("").lower()
while True:
	if statement == 'ipcam':
		print('IPCAM: Pulling up cameras...')
		webbrowser.open_new_tab('http://www.insecam.org/en/byrating/')
		print("HackBox: Anything I can do for you?")
	elif 'country' in statement:
		print('IPCAM: Pulling up cameras in', statement, '...')
		statement =statement.replace("country ", "")
		webbrowser.open_new_tab('http://www.insecam.org/en/bycountry/{}'.format(statement))
		print("HackBox: Anything I can do for you?")
	elif 'place' in statement:
		print('IPCAM: Pulling up cameras in', statement, '...')
		statement =statement.replace("place ", "")
		webbrowser.open_new_tab('http://www.insecam.org/en/bytag/{}'.format(statement))
		print("HackBox: Anything I can do for you?")
	elif 'city' in statement:
		print('IPCAM: Pulling up cameras in the', statement, '...')
		statement =statement.replace("city ", "")
		webbrowser.open_new_tab('http://www.insecam.org/en/bycity/{}'.format(statement))
		print("HackBox: Anything I can do for you?")
	elif 'cameratype' in statement:
		print('IPCAM: Pulling up cameras in', statement, '...')
		statement =statement.replace("cameratype ", "")
		webbrowser.open_new_tab('http://www.insecam.org/en/bytype/{}'.format(statement))
		print("HackBox: Anything I can do for you?")
	elif 'help' in statement:
		print("-----------------------------------------------------------------")
		print(" --- General Config ---")
		print("'Country __': Searches for cameras in said country, Please Use 2 letter code for countries")
		print("EX: 'country RU' for Russia")
		print('')
		print("'Place ___'                       : Pulls up cameras in certain places")
		print("EX: 'Place beach' to search a beach")
		print('')
		print("'City ___'                        : Pulls up cameras in Cities with open cams")
		print('')
		print("'Cameratype ___'                  : Pulls up cameras made by specific manufacturers, may be useful if exploit for") 
		print("                                    said camera is discovered")
		print("-----------------------------------------------------------------")

		print("HackBox: Anything I can do for you?")

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