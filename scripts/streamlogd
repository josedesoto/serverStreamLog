#!/bin/bash
#
### BEGIN INIT INFO
# Provides:          streamLog
# Required-Start:    $syslog $local_fs $network
# Required-Stop:     $syslog $local_fs $network
# Should-Start:      $remote_fs $named
# Should-Stop:       $remote_fs $named
# Default-Start:        2 3 4 5
# Default-Stop:         0 1 6
# Short-Description:    To run the steam log app.
### END INIT INFO
#By Jose de Soto

#Paramaters we should changes.
#NOTE: name script = Provides option
NAME_APP="Stream Log"
USER_RUN_COMMAND=streamlog
COMMAN_TO_START="/opt/ServerStreamLog/init.py &"
COMMAN_TO_STOP=/opt/ed/atoz/current/script/batch-all-opcos.sh



case "$1" in
start)
	#We execute the command
	su -s /bin/bash $USER_RUN_COMMAND -c "$COMMAN_TO_START"
	if [ $? -eq 0 ] ; then
		echo "$NAME_APP with status OK"
	else
		echo "There is a problem in $NAME_APP"
		
	fi

    ;;
stop)
     	su -s /bin/bash $USER_RUN_COMMAND -c "$COMMAN_TO_STOP"
	if [ $? -eq 0 ] ; then
		echo "$NAME_APP with status OK"
	else
		echo "There is a problem in $NAME_APP"	
	fi

    ;;
restart)
	stop
	sleep 3
	start     	

    ;;


*)
    echo "usage: $0 (start|stop|restart)"
esac
