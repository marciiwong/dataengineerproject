import config as config
import uuid
import ast

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID, JSON, JSONB


class Connection(object):
    def __init__(self):
        # create a db connection
        engine = create_engine(config.DB_CONNECTION_STRING_WAREHOUSE)
        self.engine = engine

    def get_session(self):
        Session = sessionmaker(bind=self.engine)

        return Session()

    def get_engine(self):
        return self.engine


Base = declarative_base()


def init_db():
    # create a db connection
    engine = create_engine()
    Base.metadata.create_all(bind=engine)

class Users(Base):

    __tablename__ = 'users'
    __table_args__ = {'schema': 'raw'}

	# define required database columes
    user_id = Column(UUID, primary_key=True)
    seed = Column(String)
    gender = Column(String)
    name = Column(JSONB)
    location = Column(JSONB)
    email = Column(String)
    login = Column(JSONB)
    dob = Column(JSONB)
    registered = Column(JSONB)
    phone = Column(String)
    cell = Column(String)
    id = Column(JSONB)
    picture = Column(JSONB)
    nat = Column(String)

