__author__ = 'cui'

import hashlib

action_root_prefix = '[ACTION_ROOT]'
action_root_main_parent = action_root_prefix + 'MAIN_MENU'
action_root_title_parent = action_root_prefix + 'TITLE_MENU'


def to_md5(key):
    hash = hashlib.md5()
    hash.update(key)
    return hash.hexdigest()