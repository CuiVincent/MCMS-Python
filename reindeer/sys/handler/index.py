__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import tornado.web
import reindeer.sys.base

class IndexHandler(reindeer.sys.base.BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.render('sys/index.html')
