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
    left = 0
    right = pattern_size

    while right < len(seq):
        for idx in range (pattern_size):
            if pattern[idx] != seq[left + idx]:
                break
        else:
            position.append((left + pattern_size)//2)
        left += 1
        right += 1

    return position

def binary_search(seq, number):
    # ordered_numbers
    left = 0
    right = len(seq)-1

    while left <= right:
        middle = (left + right) //2

        if seq[middle] == number:
            return middle
        elif seq[middle]<number:
            left = middle +1
        elif seq[middle] > number:
            right = middle -1

    return None




def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    result_1= linear_search(sequential_data, 7)
    print(result_i)

    sequential_data = read_data("sequential.json", "dna_sequence")
    print(sequential_data)
    result_2 = pattern_search(sequential_data, "ATA")
    print(result_2)

    sequential_data = read_data("sequential.json", "ordered_numbers")
    print(sequential_data)
    result_3 = binary_search(sequential_data, 12)
    print(result_3)

if __name__ == '__main__':
    main()