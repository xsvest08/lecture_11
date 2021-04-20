import os
import json

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

    if field not in {"unordered_numbers","ordered_numbers", "dna_sequence"}:
        return None

    with open (file_name, "r") as json_file:
        dict = json.load(json_file)

    return dict[field]

def linear_search(seq, num):
    indices = []
    count = 0

    for idx in range (len(seq)):
        if seq[idx] == num:
            indices.append(idx)
            count += 1

    return {"position": indices,
            "count": count}


def pattern_search(seq,pattern):
    position = set()
    pattern_size = len(pattern)
    for idx in range (len(seq)):
        if seq[idx:idx+pattern_size] == pattern:
            position.append((idx + pattern_size)//2)
    return position

def main():

    sequential_data = read_data("sequential.json", "dna_sequence")
    print(sequential_data)

    result_i= linear_search(sequential_data, 7)
    print(result_i)

    sequential_data_2 = pattern_search(sequential_data, "ATA")
    print(sequential_data_2)
if __name__ == '__main__':
    main()