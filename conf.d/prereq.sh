#run me as sudo
#pip install pipwin
echo "Enter your package manager"
read packman
## Program install
$packman install dsniff -y
$packman install thc-hydra -y
$packman install python3 -y
$packman install mariadb -y
$packman install mariadb-server -y



##python2 install
$packman install python2.7 -y
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py
pip install --upgrade pip
pip install --upgrade setuptools
pip2 install impacket

## Python Install
pip3 install --upgrade pip setuptools wheel
pip3 install mysql.connector
#python -m pip install speechrecognition
python -m pip install pyttsx3
python -m pip install wikipedia
#python -m pip install ecapture
#python -m pip install wolframalpha
python -m pip install keyboard
#python -m pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl


#mysql setupscript

mysql_secure_installation

pause
