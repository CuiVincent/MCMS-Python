__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from sqlalchemy import Column, String, Integer
from sqlalchemy.exc import IntegrityError
from reindeer.util.common_util import to_md5
from reindeer.sys.base_db_model import BaseDbModel, new_alchemy_encoder
from reindeer.sys.exceptions import BusinessRuleException
import json


class SysUser(BaseDbModel):
    __tablename__ = 'RA_SYS_USER'
    CODE = Column(String(100), unique=True)
    NAME = Column(String(100))
    PASSWORD = Column(String(100))
    STATUS = Column(String(1), default='1')

    @classmethod
    def add(cls, user_code, user_name, pass_wd):
        user = SysUser(CODE=user_code, NAME=user_name, PASSWORD=to_md5(pass_wd) if pass_wd else '')
        cls.db_session.add(user)
        try:
            cls.db_session.commit()
        except IntegrityError:
            cls.db_session.rollback()
            raise BusinessRuleException(1051)
            # 先回滚再抛出异常，否则会滚会失败
        except:
            cls.db_session.rollback()
        if (user.ID):
            return user
        else:
            return None

    @classmethod
    def get_by_code(cls, user_code):
        item = cls.db_session.query(SysUser).filter(SysUser.CODE == user_code).first()
        return item

    @classmethod
    def get_by_id(cls, user_ID):
        item = cls.db_session.query(SysUser).filter(SysUser.ID == user_ID).first()
        return item

    @classmethod
    def get_all(cls):
        item = cls.db_session.query(SysUser).all()
        return item

    @classmethod
    def get_all_json(cls):
        r_json = []
        items = SysUser.get_all()
        for item in items:
            r_json.append(item)
        return json.dumps(r_json, cls=new_alchemy_encoder(), check_circular=False)