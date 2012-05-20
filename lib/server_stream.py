#!/usr/bin/env python


from comet_messaging import comet_send
from comet_messaging import DistributeHandler
from comet_messaging import PostHandler
from comet_messaging import TokenHandler
import tornado.httpserver
import tornado.ioloop
from config import Config


conf=Config()
KEY_CLIENT=conf.getClientKey()
PORT=conf.getServerPort()
LISTEN=conf.getServerListen()

def serverStream():
     
    DistributeHandler.tokens=False
    urls=[
        (r'/', PostHandler),
        (r'/token', TokenHandler),
        (r'/realtime/(.*)', DistributeHandler)]
    
    application = tornado.web.Application(urls, auto_reload=True)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(int(PORT), LISTEN)
    tornado.ioloop.IOLoop.instance().start()
    
def clientStream(txt, group):
    ''' Prints received text '''
    #Line with Java script
    #comet_send('http://localhost:'+str(PORT), 'oTable.fnAddData("'+str(txt).replace("\n", "")+'")', KEY_CLIENT , group)
    #Line sending plain text
    comet_send('http://localhost:'+str(PORT), str(txt).replace("\n", ""), KEY_CLIENT , group)
