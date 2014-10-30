__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from sqlalchemy import Column, String, Integer
from reindeer.sys.base_db_model import BaseDbModel
from reindeer.sys.exceptions import BusinessRuleException
from reindeer.util import common_util
from reindeer.sys.model.sys_group_action import SysGroupAction
from reindeer.sys.model.sys_group_user import SysGroupUser


class SysAction(BaseDbModel):
    __tablename__ = 'RA_SYS_ACTION'
    NAME = Column(String(100))
    TYPE = Column(String(2), default='0')
    URL = Column(String(200))
    DES = Column(String(1000))
    PARENT = Column(String(50), default=common_util.action_root_main_parent)
    LOG = Column(String(1), default='1')
    SORT = Column(Integer)
    ICON_TYPE = Column(String(1), default='0')
    ICON = Column(String(200))


    @classmethod
    def add(cls, name=None, type=None, url=None, des=None, parent=None, log=None, sort=None, icon_type=None, icon=None):
        action = SysAction(NAME=name, TYPE=type, URL=url, DES=des, PARENT=parent, LOG=log, SORT=sort,
                           ICON_TYPE=icon_type,
                           ICON=icon)
        if not str(action.PARENT).startswith(common_util.action_root_prefix):
            if not cls.get_by_ID(action.PARENT):
                raise BusinessRuleException(1101)
        cls.db_session.add(action)
        try:
            cls.db_session.commit()
        except:
            cls.db_session.rollback()
        if (action.ID):
            return action
        else:
            return None


    @classmethod
    def get_by_ID(cls, id):
        item = cls.db_session.query(SysAction).filter(SysAction.ID == id).first()
        return item

    @classmethod
    def get_tree_by_user_and_parent(cls, user_id, parent):
        sql = "select concat('" + user_id + "' ,'') as user_id ,t.*  from " + SysAction.__tablename__ + "  t , (select distinct gp.ACTION id from " + SysGroupAction.__tablename__ + " gp, " + SysGroupUser.__tablename__ + " ug where ug.USER ='" + user_id + "' and ug.GROUP = gp.GROUP) b  where b.id=t.ID and t.PARENT='" + parent + "'  order by t.sort asc"
        return cls.db_engine.execute(sql)



