__author__ = 'CuiVincent'

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app_settings import db_settings


class DatabaseInstance:
    def __init__(self, settings=db_settings, base_db_model_class=[]):
        self.__db_engine = None
        self.__db_session = None
        self.__base_db_model_classes = []
        DatabaseUtil.create_db_session(self, settings)
        self.add_base_db_model_classes(base_db_model_class)

    def bind(self, engine, session):
        self.__db_engine = engine
        self.__db_session = session

    def add_base_db_model_classes(self, base_db_model_class):
        new_classes = not isinstance(base_db_model_class, list) and [
            base_db_model_class] or base_db_model_class
        for clazz in new_classes:
            if clazz not in  self.__base_db_model_classes:
                clazz.db_session = self.__db_session
                self.__base_db_model_classes.append(clazz)

    @property
    def db_engine(self):
        return self.__db_engine

    @property
    def db_session(self):
        return self.__db_session

    @property
    def base_db_model_classes(self):
        return self.__base_db_model_classes

    def create_all_table(self):
        DatabaseUtil.create_all_table(self)

    def drop_all_table(self):
        DatabaseUtil.drop_all_table(self)


class DatabaseUtil:
    @staticmethod
    def get_db_url(settings):
        url = ''
        if settings['driven'].lower() == 'mysql':
            url = 'mysql://' + settings['user'] + ':' + settings['password'] + '@' + settings['host'] + '/' + \
                  settings['database']
        else:
            pass
        return url

    @staticmethod
    def create_db_session(db_instance, settings):
        db_engine = create_engine(DatabaseUtil.get_db_url(settings), pool_recycle=60,
                                  connect_args={"charset": "utf8"}, echo=True)
        db_session = scoped_session(sessionmaker(bind=db_engine))
        db_instance.bind(db_engine, db_session)

    @staticmethod
    def create_all_table(db_instance):
        for clazz in db_instance.base_db_model_classes:
            clazz.metadata.create_all(bind=db_instance.db_engine)

    @staticmethod
    def drop_all_table(db_instance):
        for clazz in db_instance.base_db_model_classes:
            clazz.drop_all(bind=db_instance.db_engine)



