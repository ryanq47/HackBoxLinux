#run me as sudo

echo "Enter your package manager"
read packman
## Program remove

$packman remove thc-hydra
$packman remove dsniff
#$packman remove python3 -- leaving python because it's usually needed on linux for something

#python -m pip uninstall speechrecognition
python -m pip uninstall pyttsx3
python -m pip uninstall wikipedia
#python -m pip uninstall ecapture
python -m pip uninstall wolframalpha
#python -m pip uninstall PyAudio-0.2.11-cp38-cp38-win_amd64.whl

pause
