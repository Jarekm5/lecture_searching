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
    list_for = []
    o = 0
    for i, value in enumerate(sekv):
        if number == value:
            list_for.append(i)
            dict["index"] = list_for
            o += 1
    dict["count"] = o
    return dict

def pattern_search(seq, pattern):
    mnoz = {}
    list_seq = []
    ranges = len(pattern)
    for i in range(len(seq)- ranges + 1):
        if seq[i:i + ranges] == pattern:
            list_seq.append(i)
    mnoz["index"] = list_seq
    return mnoz

def binary_search(seq, num):



def main():
    readed_unordered = read_data("sequential.json", "unordered_numbers")
    linear_search(readed_unordered, 5)
    readed_dna = read_data("sequential.json", "dna_sequence")
    pattern_search(readed_dna, "ATA")
    readed_ordered = read_data("sequential.json", "ordered_numbers")
    binary_search(readed_ordered, 6)
    pass


if __name__ == '__main__':
    main()
