#!/usr/bin/env python


#import  lib.server_stream import start
from   lib.server_stream import clientStream
from   lib.server_stream import serverStream
import threading
from lib.tail import Tail
from lib.config import Config



if __name__ == "__main__":
    #start()
    conf=Config()
    DELAY_TIME=conf.getClientDelay_time()
    LOGS=conf.getLogs()
    try:
        #We start the clients
        for group, path in LOGS:
                print "init logs: " + path
                t = Tail(path, group)
                t.register_callback(clientStream)
                threading.Thread(target=t.follow, args=(DELAY_TIME,)).start()
                
        #Start the server!!!
        #threading.Thread(target=serverStream()).start()
        serverStream()
        
    except IOError as (errno, strerror):
        print "I/O error({0}): {1}".format(errno, strerror)
        
            