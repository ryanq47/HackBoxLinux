Beta 1.1 - Functional, with new modules, but not production ready - explore the Proof Of Concept branch for latest updates!

Disclaimer! This software is provided for educational use only! I do not take responsibility for any illegal, malicious, or unethical acts performed using this software!

Note: I am learning python while making this program, do not assume in any way shape or form that this software is secure, reliable, or safe to have on your system. Use at your own risk!



Alright now to the fun stuff:

### Attack Mode: For offensive security <br/>
- ####   System Access: All Sorts of ways to get into a system! <br/>
    -- Protocol Cracker: A hydra based bruteforce program to brute force logins, Note!: It is fairly slow and is best to use on simple/default passwords only<br/> 
    
    -- EternalBlue: This is the infamous eternal blue exploit, it works on windows 7, and 10 (provided you can get a payload that avoids Windows Defender). <br/>


    --  AutoTack: An automated scanner, and attacker! <br/>
        -- AutoTack is a combination of everyhing in HackBox. It uses other modules code (such as protocol cracker) to scan, store and attack targets automatically. Currently, only bruteforce attacks are supported, but more are coming!

- ####   Denial of Service: Preventing people from being productive <br/>
    -- MITM ArpSpoof: A dsniff powered tool that will perform a MITM Arp attack, denying any internet to the selected device  
            Pro Tip: This works on routers too...  with varying effects. Have fun! (Use the router's IP as the target address) 

- ####   Script Runner: A module with preconfigured security scripts! <br/>
    -- A spare shell version of ArpSpoof is here (It was originally coded in bash then converted to python)
    -- fail2ban.sh: An interactive fail2ban install & setup script.
    -- reverse_shell scripts: any script with 'rev_shell' on it sets up a reverse shell, each with a different method  

### Defense Mode <br/>
    -- A work in progress, nothing here yet, but some to come in future updates

### Recon Mode: For reconnaissance <br/>
- ####   Surveillance: A set of modules based around Open Source Intellegence (OSINT) <br/>
    -- IP-CAM: A collection of publicy accessible cameras in hundreds of countries 
    -- UserCheck: A simple module that will check where a username is being used 

- 



## Remote Access
- Through netcat, you can forward a remote HackBox instance to your local machine, no install needed!
    To do this, on your Host machine, run nc -e ./HackBox.py IPADDRESS PORT
    Then on your local machine, run nc -nvlp PORT
    A hackbox instance should then appear on screen
    Note: Local attacks shouldn't work if doing this, as HackBox is running on the Remote Machine, not locally
    Note pt 2: This essentially opens a reverse shell on your machine... so be incredibly careful when doing this
