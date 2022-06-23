import os
import json


## sample JSON formatting for autotack, each variable would come from autotack, then the expanded JSON below it will write it 

## Testing --
## to the DB file
ipaddr = '192.168.1.1'
ports = ['1','22','443']
services = ['ICMP','SSH','HTTPS']


## Vars

DB_name = "hackbox_db" ## Best to put application name here or if in hackbox, keep it hackbox_db)
TABLE_name = "hackbox_ip_table"

data = {

            'ip_addr' : ipaddr,
            'open_ports' : ports,
            'services' : services
}


def CreateDB(DB_name):
        try:
            os.mkdir("Database/" + DB_name) #0o777)
            ## Note, if using outside of hackbox, create a folder called Database in the current working directory
        except:
            print('DB "' + DB_name + '" ready to go')
        ## 0o644 allows creator to  read + write, but everyone else to only read. maybe in future make option to choose diff levels of security (640, 600 etc)

        
def CreateTABLE(DB_name,TABLE_name):
        try:
            os.mkdir("Database/"+ DB_name + '/' + TABLE_name)
        except:
            print('Duplicate table detected, using previously created "' + TABLE_name + '"')



            
def writeCOLUMN(DB_name,TABLE_name,COLUMN_name,COLUMN_contents):
        with open("Database/" + DB_name + '/' + TABLE_name + '/' + COLUMN_name, 'w') as c:
            jsondata = COLUMN_contents
            json.dump(jsondata, c)
        #Note this will overwrite existing file contents

def readCOLUMN(DB_name,TABLE_name,COLUMN_name,COLUMN_value):
        r = open("Database/" + DB_name + '/' + TABLE_name + '/' + COLUMN_name, "r")
        json_str = (r.read())
        data = json.loads(json_str)
        readCOLUMN.key_data = (data[COLUMN_value])
        print("----------------------------------------")
        print(readCOLUMN.key_data)
        
CreateDB(DB_name)
CreateTABLE(DB_name, TABLE_name)
writeCOLUMN(DB_name, TABLE_name, ipaddr, data)
readCOLUMN(DB_name,TABLE_name, ipaddr , 'ip_addr')