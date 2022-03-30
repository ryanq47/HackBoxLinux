echo "PingSweep"
echo""

echo '----------'
route -n
echo '----------'

echo""

echo "Enter the first 3 octets of your default gateway - ex '192.168.0'"
read defaultgateway



for i in {1..254}
do (ping -c 1 $defaultgateway.$i | grep "bytes from" &)
done

#for i in {1..254} ;do (ping -c 1 192.168.1.$i | grep "bytes from" #&) ;done
