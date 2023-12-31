from pathlib import Path
import os

from sqlalchemy import MetaData, Table
from sqlalchemy.schema import CreateSchema
from model import Connection, Base
import config as config

# Initialize directory and csv file
# create them if does not exist programatically
def init_csv_file():

    Path(config.CSV_FILE_DIR).mkdir(parents=True, exist_ok=True)
    

# Initialize schema and table
def init_db():
    # Establish a db connection
    # get db session
    # create a schema named raw
    # create users table in schema raw with appropiate columns
    # commit db
    # close db  
    conn = Connection()
    engine = conn.get_engine()

    schema_name = 'raw'
    if not engine.dialect.has_schema(engine, schema_name):
        engine.execute(CreateSchema(schema_name, if_not_exists=True))

    metadata = MetaData()
    users_table = Table('users', metadata, autoload_with=engine, schema='raw')
    users_table.drop(engine)
    
    Base.metadata.create_all(engine)



if __name__ == '__main__':
    init_csv_file()
    init_db()
