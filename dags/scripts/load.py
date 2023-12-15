import pandas as pd
from pathlib import Path
import ast

from model import Connection, Users
import config


def get_file_path():
    # should return a os file path with correct destination.
    # Do not change file name
    # filename = "random_user.csv"
    # write your code here
    dir = Path(config.CSV_FILE_DIR)
    file_path = dir / 'random_user.csv'
    return file_path


def main():

    filename = get_file_path()
    # read the csv file
    # Create user object
    # insert the user object in the array
    data = pd.read_csv(filename)
    cols = ['user_id', 'seed', 'gender', 'name', 'location', 'email', 'login', 'dob', 'registered', 'phone', 'cell', 'id', 'picture', 'nat']
    data = data[cols]
    json_cols = ['name', 'location', 'login', 'dob', 'registered', 'id', 'picture']
    for i in json_cols:
        data[i] = data[i].apply(lambda x: ast.literal_eval(x))

    data_insert = data.to_dict('records')

    # Connect with the db
    # get a sessions
    # First delete all previous users table data from schema raw
    # bulk load data
    # commit db
    # close db
    # write your code here
    conn = Connection()
    session = conn.get_session()
    session.bulk_save_objects([Users(**row) for row in data_insert])
    session.commit()
    session.close()



if __name__ == '__main__':
    main()
