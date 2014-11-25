__author__ = 'CuiVincent'
# -*- coding: utf8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid
import json
from sqlalchemy.ext.declarative import DeclarativeMeta

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


def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    try:
                        if isinstance(data, datetime):
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                        json.dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:
                        pass
                        # fields[field] = None
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder