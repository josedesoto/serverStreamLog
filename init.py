#!/usr/bin/env python


#import  lib.server_stream import start
from   lib.server_stream import clientStream
from   lib.server_stream import serverStream
import threading
from lib.tail import Tail
from lib.config import Config

import logging

'''

    logger.critical('This is a critical message.')
    logger.error('This is an error message.')
    logger.warning('This is a warning message.')
    logger.info('This is an informative message.')
    logger.debug('This is a low-level debug message.')
'''

if __name__ == "__main__":
    #start()
    
    
    conf=Config()
    DELAY_TIME=conf.getClientDelay_time()
    LOGS=conf.getLogs()
    
    LOGGING_LEVELS = {'critical': logging.CRITICAL,
                  'error': logging.ERROR,
                  'warning': logging.WARNING,
                  'info': logging.INFO,
                  'debug': logging.DEBUG}

    try:
        logging_level = LOGGING_LEVELS.get(conf.getServerLog_level(), logging.NOTSET)
        logging.basicConfig(filename=str(conf.getServerLog()), level=logging_level, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("STARTING SERVER STREAM LOG...")
        
    except IOError as (errno, strerror):        
        logging.error("I/O error({0}): {1}".format(errno, strerror))
        logging.error("Trying to open log for logging: " +conf.getServerLog())
        exit(2);
        
        
    try:
        #We start the clients
        for group, path in LOGS:
         
                logging.info("LOG: " + path + " readed from config file")
                t = Tail(path, group, DELAY_TIME)
                if t.check_file_validity():
                    logging.info("TAIL LOAD FOR: " + path)
                    t.register_callback(clientStream)
                    threading.Thread(target=t.follow,).start()
                    
        #Start the server!!!
        #threading.Thread(target=serverStream()).start()
        serverStream()
        logging.info("SHUTING DOWN SERVER STREAM LOG...")
        
    except IOError as (errno, strerror):
        logging.error("I/O error({0}): {1}".format(errno, strerror))
        exit(2);
        
            