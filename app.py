__author__ = 'CuiVincent'
# encoding:utf-8

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options

import reindeer.sys.base_handler
from app_settings import app_settings
from app_urls import app_urls
from reindeer.util.database_util import DatabaseUtil

define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self, handlers, **settings):
        tornado.web.Application.__init__(self, handlers, **settings)
        tornado.web.ErrorHandler = reindeer.sys.base_handler.ErrorHandler
        self.db_util = DatabaseUtil()
        self.db_session = self.db_util.db_session

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(app_urls, **app_settings))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
