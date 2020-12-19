import re
from sys import argv, stdin

from pymongo import MongoClient


def main():
    """
    How to insert find dict:
    * Windows: echo { "key1": "value 1", "key2": "value 2" } | python main.py
    * Linux: echo '{ "key1": "value 1", "key2": "value 2" }' | python main.py
    """

    # Read data

    option = read_input_argv()
    data = read_data_from_mongo(option)

    # Print results

    for document in data:
        print(document)


def read_input_argv() -> dict:
    """
    Read provided input arguments.

    Returns
    -------
    option : dict
        Dict containing parsed input arguments.
    """

    if len(argv) != 5:
        raise ValueError(f"Expected 4 arguments, received {len(argv) - 1}")

    option = {
        'host': argv[1],
        'port': int(argv[2]),
        'database': argv[3],
        'collection': argv[4]
    }
    if stdin.isatty() and type(stdin) == dict:
        option['find'] = stdin

    return option


def read_data_from_mongo(option: dict = None) -> list:
    """
    Connect to MongoDB and return selected documents.

    Parameters
    ----------
    option : dict
        Dict containing input arguments.

    Returns
    -------
    data : list
        List of dict with requested documents.
    """

    find = option['find'] if option.get('find') else {}
    mongo = MongoClient(option['host'], option['port'])

    return [element for element in mongo[option['database']][option['collection']].find(find)]


if __name__ == '__main__':
    main()
