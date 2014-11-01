__author__ = 'cui'

import hashlib

def to_md5(key):
    hash = hashlib.md5()
    hash.update(key)
    return hash.hexdigest()