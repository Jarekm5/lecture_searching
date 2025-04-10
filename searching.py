import os
import json

from generators import unordered_sequence

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_name, "r", encoding="utf8") as file:
        read = json.load(file)
        read = read[field]
    return print(read)

def main():

    pass


if __name__ == '__main__':
    main()
    read_data("sequential.json", "unordered_numbers")