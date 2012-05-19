#!/bin/bash
#
#Small script to install in linux the stream log server
#by Jose de Soto

#You have to be root:
if [ "$(id -u)" != "0" ]; then
	echo "This script must be run as root"
	exit 1
fi

LAST_SOURCE_CODE=https://github.com/josedesoto/serverStreamLog/blob/master/dist/ServerStreamLog-last.tar.gz
CONFIG_FILE=https://github.com/josedesoto/serverStreamLog/blob/master/etc/streamlog.cfg
INIT_FILE=https://github.com/josedesoto/serverStreamLog/blob/master/scripts/streamlogd


#We create the user to streanm log
useradd -c "Stream Log User" --shell /bin/false streamlog

#We install tonado
easy_install tornado
 
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
chmod 755 streamlogd


