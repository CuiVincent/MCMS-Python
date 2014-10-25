from reindeer.sys.exception import BusinessRuleException

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
        if usercode == 'cui' and passwd == '111':
            res = {'success': True}
            self.set_secure_cookie('user_id', str(usercode), expires_days=7)
            self.set_secure_cookie('user_name', str(usercode), expires_days=7)
        elif usercode == '1':
           raise BusinessRuleException(1001)
        elif usercode == '2':
           raise BusinessRuleException(1002)
        elif usercode == '3':
           raise BusinessRuleException(1003)
        else:
           raise BusinessRuleException(1111)
        return self.write(json_encode(res))