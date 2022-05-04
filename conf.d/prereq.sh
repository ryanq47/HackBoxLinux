#run me as sudo/root!!!!
#Note: This is catered towards kali... I haven't put the time into making an installfor other distros

echo "Enter your package manager"
read packman

echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee /etc/apt/sources.list
apt-get update

## Program install
$packman install dsniff -y
$packman install thc-hydra -y
$packman install python3 -y
$packman install mariadb -y
$packman install mariadb-client -y
$packman install mariadb-server -y



##python2 install
$packman install python2.7 -y
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py # --> installing pip2
pip install --upgrade pip
pip install --upgrade setuptools
pip2 install impacket
rm -rf get-pip.py

## Python3 Install stuff
wget https://bootstrap.pypa.io/get-pip.py # --> installing pip3
python3 get-pip.py
rm -rf get-pip.py

pip install --upgrade pip setuptools wheel
pip install mysql.connector
pip install mysql
#python -m pip install speechrecognition
python -m pip install pyttsx3
python -m pip install wikipedia
#python -m pip install ecapture
#python -m pip install wolframalpha
python -m pip install keyboard
#python -m pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl


#mysql setupscript
systemctl start mariadb
mysql_secure_installation




# Extra packages that may be needed
#sudo apt-get install libmariadb-dev
#apt install libmariadb-dev-compat



