#!/usr/bin/python
"""
This file is part of the web2py Web Framework
Copyrighted by Massimo Di Pierro <mdipierro@cs.depaul.edu>
License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)

Attention: Requires Chrome or Safari. For IE of Firefox you need https://github.com/gimite/web-socket-js

Acknowledgements:
Tornado code inspired by http://thomas.pelletier.im/2010/08/websocket-tornado-redis/

"""


import tornado.websocket
import tornado.web
import hmac
import urllib
import time
from config import Config
import logging

listeners = {}
names = {}
tokens = {}
conf=Config()
#We get the key from the server
hmac_key=conf.getServerKey()



def comet_send(url,message,hmac_key=None,group='default'):
    sig = hmac_key and hmac.new(hmac_key,message).hexdigest() or ''
    params = urllib.urlencode({'message': message, 'signature': sig, 'group':group})
    f = urllib.urlopen(url, params)
    data= f.read()
    f.close()
    return data


class PostHandler(tornado.web.RequestHandler):
    """
    only authorized parties can post messages
    """
    
    def post(self):
        if hmac_key and not 'signature' in self.request.arguments: return 'false'
        if 'message' in self.request.arguments:
            message = self.request.arguments['message'][0]
            group = self.request.arguments.get('group',['default'])[0]
            logging.info('%s:MESSAGE to %s:%s' % (time.time(), group, message))
            if hmac_key:
                signature = self.request.arguments['signature'][0]
                if not hmac.new(hmac_key,message).hexdigest()==signature: return 'false'
            for client in listeners.get(group,[]): client.write_message(message)
            return 'true'
        return 'false'

class TokenHandler(tornado.web.RequestHandler):
        
    """
    if running with -t post a token to allow a client to join using the token
    the message here is the token (any uuid)
    allows only authorized parties to joins, for example, a chat
    """
    def post(self):
        if hmac_key and not 'message' in self.request.arguments: return 'false'
        if 'message' in self.request.arguments:
            message = self.request.arguments['message'][0]
            if hmac_key:
                signature = self.request.arguments['signature'][0]
                if not hmac.new(hmac_key,message).hexdigest()==signature: return 'false'
            tokens[message] = None
            return 'true'
        return 'false'

class DistributeHandler(tornado.websocket.WebSocketHandler):
    def open(self,params):
        group,token,name = params.split('/')+[None,None]
        self.group = group or 'default'
        self.token = token or 'none'
        self.name = name or 'anonymous'
        # only authorized parties can join
        if DistributeHandler.tokens:
            if not self.token in tokens or not token[self.token]==None:
                self.close()
            else:
                tokens[self.token] = self
        if not self.group in listeners: listeners[self.group]=[]
        # notify clients that a member has joined the groups
        for client in listeners.get(self.group,[]): client.write_message('+'+self.name)
        listeners[self.group].append(self)
        names[self] = self.name
        logging.info('%s:CONNECT to %s' % (time.time(), self.group))
    def on_message(self, message):
        pass
    def on_close(self):
        if self.group in listeners: listeners[self.group].remove(self)
        del names[self]
        # notify clients that a member has left the groups
        for client in listeners.get(self.group,[]): client.write_message('-'+self.name)
        logging.info('%s:DISCONNECT from %s' % (time.time(), self.group))

