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
#Script developed for Debian distributions. Tested in Debian 6


NAME_APP="Stream Log"
USER_RUN_COMMAND=streamlog
COMMAN_TO_START="python /opt/ServerStreamLog/init.py"
COMMAN_TO_STOP="we process with a kill"

PID_FILE="/var/run/streamLog.pid"

start() {

	if ! test -e $PID_FILE
	then
		#We execute the command
		cmd="`su -s /bin/bash $USER_RUN_COMMAND -c "$COMMAN_TO_START  > /dev/null 2>&1 &"`"
		exec $cmd	
		`ps -o pid,command ax | grep "$COMMAN_TO_START" | awk '!/awk/ && !/grep/ {print $1}' | head -1 > $PID_FILE`

		if [ $? -eq 0 ] ; then
			echo "$NAME_APP with status OK"
		else
			echo "There is a problem in $NAME_APP"
		
		fi
	else
		PID=`cat $PID_FILE`
		echo "Process running with PID: $PID"
		echo "Please, check $PID_FILE"
	fi

}

stop() {

	if test -e $PID_FILE
	then
		PID=`cat $PID_FILE`
		if [ $PID != 0 ];
		then
			kill $PID
			if [ $? -eq 0 ] ; then
				rm $PID_FILE
				echo "Terminated $NAME_APP with status OK"
			else
				echo "There is a problem in $NAME_APP"	
			fi
		fi
	else
		echo "Can not stop. PID process not found"

	fi

}



case "$1" in
start)
	start
    ;;
stop)
	stop
    ;;
restart)
	stop
	sleep 2
	start  	
    ;;
	

*)
    echo "usage: $0 (start|stop|restart)"
esac
