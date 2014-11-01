__author__ = 'CuiVincent'
__all__ = ['app_urls','app_modules']

from reindeer.sys.urls import sys_urls
from reindeer.sys.urls import sys_modules

app_urls = []
app_urls.extend(sys_urls)

app_modules = {}
app_modules = dict(app_modules.items() + sys_modules.items())