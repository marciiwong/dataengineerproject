import config as config
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

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.seed = kwargs['seed']
        self.gender = kwargs['gender']
        self.name = ast.literal_eval(kwargs['name'])
        self.location = ast.literal_eval(kwargs['location'])
        self.email = kwargs['email']
        self.login = ast.literal_eval(kwargs['login'])
        self.dob = ast.literal_eval(kwargs['dob'])
        self.registered = ast.literal_eval(kwargs['registered'])
        self.phone = kwargs['phone']
        self.cell = kwargs['cell']
        self.id = ast.literal_eval(kwargs['id'])
        self.picture = ast.literal_eval(kwargs['picture'])
        self.nat = kwargs['nat']
