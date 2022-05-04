#run me as sudo

echo "Enter your package manager"
read packman
## Program remove

$packman remove thc-hydra -y
$packman remove dsniff -y
#$packman remove python3 -- leaving python because it's usually needed on linux for something
$packman remove python2 -y
$packman remove mariadb-client -y
$packman remove mariadb -y
$packman remove mariadb-server -y

#py2
pip2 uninstall impacket


pip uninstall mysql.connector
pip uninstall mysql

#python -m pip uninstall speechrecognition
pip uninstall pyttsx3
pip uninstall wikipedia
#python -m pip uninstall ecapture
pip uninstall wolframalpha
#python -m pip uninstall PyAudio-0.2.11-cp38-cp38-win_amd64.whl


