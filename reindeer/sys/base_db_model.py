__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid

BaseDbModel = declarative_base(name='BaseDbModel')
BaseDbModel.ID = Column(String(50), primary_key=True)
BaseDbModel.C_USER = Column(String(50), default='[UNKNOW]')
BaseDbModel.C_DATE = Column(DateTime, default=datetime.now())
original_init = BaseDbModel.__init__


def new_init(self, *args, **kwargs):
    original_init(self, *args, **kwargs)
    if not self.ID:
        self.ID = uuid.uuid1()


BaseDbModel.__init__ = new_init


def set_c_user(self, c_user):
    self.C_USER = c_user


BaseDbModel.set_c_user = set_c_user
