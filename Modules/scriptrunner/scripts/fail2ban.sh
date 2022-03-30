## fail2ban install/config script 1.0 - Ryan kleffman 3/25/2022 12:35PM

echo "This needs to be run as root!!"

echo 'enter your package manager (ex yum, apt):'
read packman

$packman install fail2ban -y

echo ""

echo "Setting up .local config files"

## Note! The .conf files are the base configuration files for fail2ban
## The .local files add exceptions to that .conf file. 
## Never edit the .conf file as it will get reset/overwritten during updates

cp /etc/fail2ban/fail2ban.conf /etc/fail2ban/fail2ban.local

cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

cd /etc/fail2ban/

## Adding IP's to ignore

echo ""
echo "## --- Configuring Default Rules --- ##"
echo ""

echo "Enter IP's to ignore, or hit enter to skip:"
echo "Syntax: Seperate them with a space (192.168.1.1 192.168.1.2)"
read ipignore

echo "ignoreip = 127.0.0.1/8" $ipignore >> /etc/fail2ban/fail2ban.local

echo ""

echo "Bringing out the banhammer, Enter the defualt ban time!"
echo "Syntax: Number + Time Increment (d = days, m = minutes, none = seconds; Negative number means infinite ban)"
echo "EX: '1d' - one day, '100m'- 100 minutes, '-1' infinite"
read banhammer

echo "bantime = " $banhammer >> /etc/fail2ban/fail2ban.local

echo ""

echo "Max Retries! Enter the amount of login retries before an IP gets the boot!"
echo "Syntax: Just enter a number like '5' or '69'"
read maxretry

echo "maxretry = " $maxretry >> /etc/fail2ban/fail2ban.local
echo "findtime = 10m"  >> /etc/fail2ban/fail2ban.local

echo ""

systemctl restart fail2ban

echo "## --- Basic Setup Complete --- ##"

echo ""

echo "Your basic setup is now complete! Note that only SSH is enabled by default for fail2ban," 
echo "but you can edit those settings in '/etc/fail2ban/jail.local'"