__author__ = 'CuiVincent'
# encoding:utf-8

import tornado.web
from tornado.escape import json_encode

class ToLoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('sys/login.html')

class DoLoginHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        usercode = self.get_argument('usercode')
        passwd = self.get_argument('passwd')
        if(usercode == 'cui' and passwd == '111' ):
             res = {'success': True}
        else:
             res = {'success': False, 'msg': '错误', 'info': '错误了！'}
        return self.write(json_encode(res))