#!/bin/bash
#
#Small script to install in linux the stream log server
#by Jose de Soto

#You have to be root:
if [ "$(id -u)" != "0" ]; then
	echo "This script must be run as root"
	exit 1
fi

PROJECT_GITHUB_NAME=serverStreamLog
PROJECT_URL=https://github.com/josedesoto/serverStreamLog
PATH_TO_INSTALL=/opt

#We create the user to streanm log
useradd -c "Stream Log User" --shell /bin/false streamlog

#We install tonado
apt-get -y install curl
sleep 2
curl http://python-distribute.org/distribute_setup.py | python
sleep 2
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
sleep 2
pip install tornado
sleep 2
apt-get  install git

#We download the cource code
cd $PATH_TO_INSTALL
git clone $PROJECT_URL
chown -R streamlog:streamlog serverStreamLog

#We download the config file

if ! test -e /etc/streamlog.cfg
then
	mv $PATH_TO_INSTALL/$PROJECT_GITHUB_NAME/etc/streamlog.cfg /etc/
	rm -fr $PATH_TO_INSTALL/$PROJECT_GITHUB_NAME/etc
else
	echo "FOUND PREVIOUS /etc/streamlog.cfg. NOT OVERWRITE. UPDATE MANUALLY"
fi

#We download the init.d script 
mv $PATH_TO_INSTALL/$PROJECT_GITHUB_NAME/scripts/streamlogd.sh /etc/init.d/streamlogd
chmod 755 /etc/init.d/streamlogd

#Creating the log for debug:
touch /var/log/streamlog.log
chown streamlog:streamlog /var/log/streamlog.log




