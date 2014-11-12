__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import reindeer.sys.base_handler
from reindeer.sys.exceptions import BusinessRuleException


class UserHandler(reindeer.sys.base_handler.BaseHandler):
    def get(self):
        self.render('sys/user_list.html')

