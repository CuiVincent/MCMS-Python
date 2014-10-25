__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import reindeer.sys.base
from tornado.escape import json_encode

class LoginHandler(reindeer.sys.base.BaseHandler):
    def get(self):
        self.render('sys/login.html')

    def post(self, *args, **kwargs):
        usercode = self.get_argument('usercode')
        passwd = self.get_argument('passwd')
        if(usercode == 'cui' and passwd == '111' ):
            res = {'success': True}
        else:
            raise Exception("密码错误")
            res = {'success': False, 'msg': '错误', 'info': '错误了！'}
        return self.write(json_encode(res))