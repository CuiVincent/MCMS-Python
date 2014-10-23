__author__ = 'VincentCui'
__all__ = ['sys_urls']

from src.sys.handler import index
from src.sys.handler import login
from app_settings import app_settings

sys_urls = [
    ('/',index.SysIndexHandler),
    (app_settings['login_url'], login.ToLoginHandler ),
    ('/sys/doLogin', login.DoLoginHandler )

]