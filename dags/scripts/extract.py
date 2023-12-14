import requests
import config
import os
import multiprocessing as mp
import concurrent.futures
import pandas as pd
import uuid
from pathlib import Path


def next_seed(seed):

    # create the next permutation from the given SEED above
    # order is important here, and repetition is not allowed
    
    seed_list = list(seed)
    
    # Find the rightmost element that is smaller than the element to its right
    i = len(seed_list) - 2
    while i >= 0 and seed_list[i] >= seed_list[i + 1]:
        i -= 1
    
    # If there is no such element, the seed is the last permutation
    if i == -1:
        return None
    
    # Find the smallest element to the right of i that is greater than seed[i]
    j = len(seed_list) - 1
    while seed_list[j] <= seed_list[i]:
        j -= 1
    
    # Swap seed[i] and seed[j]
    seed_list[i], seed_list[j] = seed_list[j], seed_list[i]
    
    # Reverse the suffix starting from i + 1 to get the next permutation
    seed_list[i + 1:] = reversed(seed_list[i + 1:])
    
    return ''.join(seed_list)


def get_data(seed):

    # fetch data from API_URL defined in config and return the json data
    response = requests.get(url=config.API_URL.format(seed))
    data = response.json() if response.status_code == 200 else {'results': []}
    data['seed'] = seed

    return data


def import_data(calls=10000):
    # Use multiprocessing or thread pool or concurrency
    # to generate next seed and then make concurrent get api request and fetch single user data.
    # a total of 10000 api call need to be made
    # no api call should have same seed value.
    seed = config.SEED
    seeds = []
    for i in range(0, calls):
        seed = next_seed(seed)
        seeds.append(seed)

    with concurrent.futures.ThreadPoolExecutor(10) as executor:
        responses = executor.map(get_data, seeds)
    
    responses = list(responses)
    
    return responses


def get_file_path():
    # should return a os file path with correct destination.
    # Do not change file name
    # filename = "random_user.csv"
    dir = Path(config.CSV_FILE_DIR)
    file_path = dir / 'random_user.csv'

    return file_path


def transform_data(data_json):
    # create a pandas data frame
    # do any required pre-processing such as
    # fill-in or remove garbadge value if any
    # return data frame

    df = pd.DataFrame(data_json)
    # if info is NA, that means seed is not found in API call
    df = df[~df['info'].isna()].reset_index(drop=True)

    df['results'] = df['results'].apply(lambda x: x[0])
    expand_result = pd.json_normalize(df['results'], max_level=0)
    df = pd.concat([df, expand_result], axis=1)
    df['user_id'] = df['seed'].apply(lambda x: uuid.uuid5(uuid.uuid4(), x))
    
    return df


def save_new_data_to_csv(data):
    # save the data to a csv file
    # file should be saved in the defined location
    # filename = get_file_path()

    data.to_csv(get_file_path())



def main():

    data = import_data(calls=100)
    data = transform_data(data_json=data)
    save_new_data_to_csv(data)


if __name__ == "__main__":
    main()
