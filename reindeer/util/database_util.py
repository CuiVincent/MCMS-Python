__author__ = 'CuiVincent'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from app_settings import db_settings

Base = declarative_base()

def get_db_url(db_setting):
    url = ''
    if (db_setting['driven'].lower() == 'mysql'):
        url =  'mysql://' + db_setting['user'] + ':' + db_setting['password'] + '@' + db_setting['host'] + '/' + \
                db_setting['database']
    else:
        pass
    return url

class DatabaseUtil:

    def __init__(self):
        self.engine = create_engine(get_db_url(db_settings), pool_recycle=60, connect_args={"charset": "utf8"}, echo=True)
        self.db_session = scoped_session(sessionmaker(bind=self.engine))
        self.create_all()

    def create_all(self):
        Base.metadata.create_all(bind=self.engine)

    def drop_all(self):
        Base.metadata.drop_all(bind=self.engine)

    @property
    def session(self):
        return self.db_session

db_util = DatabaseUtil()






