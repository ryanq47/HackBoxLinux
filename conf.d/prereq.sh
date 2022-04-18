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

## Python Install
pip3 install --upgrade pip setuptools wheel

#python -m pip install speechrecognition
python -m pip install pyttsx3
python -m pip install wikipedia
#python -m pip install ecapture
python -m pip install wolframalpha
python -m pip install keyboard
#python -m pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl




pause
