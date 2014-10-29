__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from sqlalchemy import Column, String
from reindeer.sys.base_db_model import BaseDbModel


class SysGroup(BaseDbModel):
    __tablename__ = 'RA_SYS_GROUP'
    CODE = Column(String(100), unique=True)
    NAME = Column(String(100))

    @classmethod
    def add(cls, user_code, user_name):
        group = SysGroup(CODE=user_code, NAME=user_name)
        cls.db_session.add(group)
        try:
            cls.db_session.commit()
        # except IntegrityError:
        #     raise BusinessRuleException(1101)
        except:
            cls.db_session.rollback()
        if (group.ID):
            return group
        else:
            return None