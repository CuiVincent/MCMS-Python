__author__ = 'VincentCui'
# encoding:utf-8

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options
from app_settings import app_settings
from app_urls import app_urls

define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self, handlers, **settings):
        tornado.web.Application.__init__(self, handlers, **settings)


application = Application(app_urls, **app_settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
