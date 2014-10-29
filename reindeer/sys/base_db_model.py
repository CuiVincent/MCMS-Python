__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
import uuid

BaseDbModel = declarative_base(name='BaseDbModel')
BaseDbModel.ID = Column(String(50), primary_key=True)
original_init = BaseDbModel.__init__


def new_init(self, *args, **kwargs):
    original_init(self, *args, **kwargs)
    if not self.ID:
        self.ID = uuid.uuid1()


BaseDbModel.__init__ = new_init



