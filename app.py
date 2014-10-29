__author__ = 'CuiVincent'
# encoding:utf-8

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options

import reindeer.sys.base_handler
from app_settings import app_settings, db_settings
from app_urls import app_urls
from reindeer.util.database_util import DatabaseUtil, DatabaseInstance
from reindeer.sys.base_db_model import BaseDbModel

define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self, handlers, **settings):
        tornado.web.Application.__init__(self, handlers, **settings)
        tornado.web.ErrorHandler = reindeer.sys.base_handler.ErrorHandler
        self.db_instance = DatabaseInstance(db_settings, BaseDbModel)
        Application.instance = self
        DatabaseUtil.create_all_table(self.db_instance)

    @classmethod
    def instance(cls):
        return cls.instance


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(app_urls, **app_settings))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
