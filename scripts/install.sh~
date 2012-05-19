#!/bin/bash
#
#Small script to install in linux the stream log server
#by Jose de Soto

#You have to be root:
if [ "$(id -u)" != "0" ]; then
	echo "This script must be run as root"
	exit 1
fi

LAST_SOURCE_CODE=https://github.com/downloads/josedesoto/serverStreamLog/ServerStreamLog-last.tar.gz
CONFIG_FILE=https://github.com/downloads/josedesoto/serverStreamLog/streamlog.cfg
INIT_FILE=https://github.com/downloads/josedesoto/serverStreamLog/streamlogd.sh


#We create the user to streanm log
useradd -c "Stream Log User" --shell /bin/false streamlog

#We install tonado
curl http://python-distribute.org/distribute_setup.py | python
sleep 2
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
sleep 2
pip install tornado

#We download the cource code
cd /opt
wget $LAST_SOURCE_CODE
tar xzf ServerStreamLog-last.tar.gz
ln -s ServerStreamLog-last ServerStreamLog

#We download the config file

if ! test -e /etc/streamlog.cfg
then
	cd /etc
	wget $CONFIG_FILE
fi

#We download the init.d script 
cd /etc/init.d
wget $INIT_FILE
mv streamlogd.sh streamlogd
chmod 755 streamlogd


