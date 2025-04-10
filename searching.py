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
    return read

def linear_search(sekv, number):
    dict = {}
    list_for_dummies = []
    o = 0
    for i, value in enumerate(sekv):
        if number == value:
            list_for_dummies.append(i)
            dict["index"] = list_for_dummies
            o += 1
    dict["count"] = o
    return print(dict)


def main():
    readed = read_data("sequential.json", "unordered_numbers")
    linear_search(readed, 5)
    pass


if __name__ == '__main__':
    main()
