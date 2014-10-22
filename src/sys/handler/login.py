__author__ = 'VincentCui'
# encoding:utf-8

import tornado.web

class SysLoginHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('sys/login.html')
