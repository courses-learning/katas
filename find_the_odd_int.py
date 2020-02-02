"""Given an array, find the integer that appears an odd number of times.
There will always be only one integer that appears an odd number of times."""


def find_it(seq):

    unique_list = set(seq)

    for num in unique_list:
        occurances = seq.count(num)
        if occurances % 2 != 0:
            return num

    return None
