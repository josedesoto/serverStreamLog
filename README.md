Copyrighted by Jose de Soto <josedesoto@gmail.com>
License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)
Version: 1.2-alpha

Description: 
Simple stream log based in web2py code framework. The app use streaming Comet, this opens a single persistent connection from the client browser to the server 
for all Comet events.

The configuration is really easy. We only need to add logs in /etc/streamlog.cfg, for example:

		[logs]
		syslog=/var/log/syslog
		apache-vhost-shop=/var/log/apache/shop-access.log

Tested with Python 2.6 and 2.7
Tested with Ubuntu 11.10 and Debian 6

## How to install in Linux:

Note: The script will install some dependencies (curl, pip and tornado) and will create a user named stramlog
to run the server without root permissions.

1- As root user download the script install.sh:

	#wget https://raw.github.com/josedesoto/serverStreamLog/master/scripts/install.sh
	
2- Add exec permissions and execute:

	#chmod 755 install.sh
	#./install.sh
	
3- Add some logs in /etc/streamlog.cfg to create streaming
	
4- Start the service:

	#/etc/init.d/streamlogd start

## Install a client to read the logs:

	https://github.com/josedesoto/clientStreamLog


## DEMO IN GAE:

	http://streamlogs.appspot.com/streamlog


## Based on:
http://code.google.com/p/web2py/source/browse/gluon/contrib/comet_messaging.py
