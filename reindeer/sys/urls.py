__author__ = 'CuiVincent'
__all__ = ['sys_urls']

from reindeer.sys.handler import index
from reindeer.sys.handler import login
from app_settings import app_settings

sys_urls = [
    (r'/',index.IndexHandler),
    (app_settings['login_url'], login.LoginHandler )
]