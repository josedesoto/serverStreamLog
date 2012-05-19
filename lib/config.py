#!/usr/bin/env python
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('./etc/streamlog.cfg')

class Config(object):

    def getServerKey(self):   
        return config.get("server", "key")
    
    def getServerListen(self):   
        return str(config.get("server", "listen"))
    
    def getServerPort(self):   
        return int(config.get("server", "port"))
        
    def getClientDelay_time(self):
        return int(config.get("client", "delay_time"))
    
    def getClientKey(self):   
        return config.get("client", "key")
    
    def getLogs(self):
        return config.items("logs")
