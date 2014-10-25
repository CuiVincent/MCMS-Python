__author__ = 'CuiVincent'
# encoding:utf-8

import tornado.web

class IndexHandler(tornado.web.RequestHandler):

    @tornado.web.authenticated
    def get(self):
        self.render('sys/index.html')
