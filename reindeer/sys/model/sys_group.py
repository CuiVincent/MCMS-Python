__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from sqlalchemy import Column, String
from reindeer.sys.base_db_model import BaseDbModel

class SysGroup(BaseDbModel):
    __tablename__ = 'RA_SYS_GROUP'
    NAME = Column(String(100))
    DES = Column(String(1000))

    @classmethod
    def add(cls, name, des):
        group = SysGroup(NAME=name, DES=des)
        cls.db_session.add(group)
        try:
            cls.db_session.commit()
        except:
            cls.db_session.rollback()
        if (group.ID):
            return group
        else:
            return None