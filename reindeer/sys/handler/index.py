__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

import tornado.web
import reindeer.sys.base_handler

class IndexHandler(reindeer.sys.base_handler.BaseHandler):

    @tornado.web.authenticated
    def get(self):
        user_name = self.get_secure_cookie('user_name')
        self.render('sys/index.html', user_name=user_name,user_menu_html=self.user_menu_html())

    def user_menu_html(self):
        return '市场反馈我觉得好吃@#￥%……&*（）（*&……%“：/.,;'