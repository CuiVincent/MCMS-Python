__author__ = 'CuiVincent'
# encoding:utf-8

from os import path

app_settings = {
    'debug': False,
    'cookie_secret': 'test',
    'login_url': r'/login',
    'xsrf_cookies': True,
    'static_path': path.join(path.dirname(__file__), 'res/static'),
    'template_path': path.join(path.dirname(__file__), 'res/templates')
}

