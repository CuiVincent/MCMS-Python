from sqlalchemy.exc import IntegrityError
from reindeer.sys.exceptions import BusinessRuleException

__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from sqlalchemy import Column, Integer, String, DateTime
from reindeer.util.common_util import to_md5
from reindeer.util.database_util import  Base,db_util

class SysUser(Base):
    __tablename__ = 'RA_SYS_USER'
    ID = Column(Integer, primary_key=True)
    CODE = Column(String(100), unique=True)
    NAME = Column(String(100))
    PASSWORD = Column(String(100))
    ISVALID = Column(String(1), default='0')
    CDATE = Column(DateTime)

    @classmethod
    def add(cls, CODE, NAME, PASSWORD):
        user = SysUser()
        user.CODE = CODE
        user.NAME = NAME
        user.PASSWORD = to_md5(PASSWORD) if PASSWORD else ''
        db_util.session.add(user)
        try:
            db_util.session.commit()
        except IntegrityError:
            raise BusinessRuleException(1101)
        except:
            db_util.session.rollback()

        if(user.ID):
            return user
        else:
            return None

    @classmethod
    def get_by_code(cls, usercode):
        item = db_util.session.query(SysUser).filter(SysUser.CODE == usercode).first()
        return item
