__author__ = 'CuiVincent'
__all__ = ['sys_urls', 'sys_modules']

from reindeer.sys.handler import index
from reindeer.sys.handler import login
from reindeer.sys.handler import user
from reindeer.sys.module import main_menu
from app_settings import app_settings

sys_urls = [
    (r'/', index.IndexHandler),
    (r'/content/(.*)', index.ContentHandler),
    (app_settings['login_url'], login.LoginHandler),
    (r'/logout', login.LogoutHandler),
    (r'/user_list', user.UserListHandler),
    (r'/user_add', user.UserAddHandler)

]

sys_modules = {'MainMenu': main_menu.MainMenuModule}