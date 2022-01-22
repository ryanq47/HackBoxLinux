sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel
cd /opt
wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz
tar xzf Python-3.8.12.tgz
cd Python-3.8.12
sudo ./configure --enable-optimizations
sudo make altinstall
sudo rm Python-3.8.12.tgz
