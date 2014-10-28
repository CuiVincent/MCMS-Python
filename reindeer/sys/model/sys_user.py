from sqlalchemy.exc import IntegrityError
from reindeer.sys.exceptions import BusinessRuleException

__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from sqlalchemy import Column, Integer, String, DateTime
from reindeer.util.common_util import to_md5
from reindeer.util.database_util import Base

class SysUser(Base):
    __tablename__ = 'RA_SYS_USER'
    ID = Column(Integer, primary_key=True)
    CODE = Column(String(100), unique=True)
    NAME = Column(String(100))
    PASSWORD = Column(String(100))
    ISVALID = Column(String(1), default='0')
    CDATE = Column(DateTime)

    @classmethod
    def add(cls, db_session, usercode, username, passwd):
        user = SysUser(CODE=usercode, NAME=username, PASSWORD=to_md5(passwd) if passwd else '')
        db_session.add(user)
        try:
            db_session.commit()
        except IntegrityError:
            raise BusinessRuleException(1101)
        except:
            db_session.rollback()
        if(user.ID):
            return user
        else:
            return None

    @classmethod
    def get_by_code(cls, db_session, usercode):
        item = db_session.query(SysUser).filter(SysUser.CODE == usercode).first()
        return item
