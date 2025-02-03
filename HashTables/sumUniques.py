#!/usr/bin/python3

from typing import List

def getUniques(list1: List[int]) -> int:
    '''function to get the unique elements of an integer list

    Args:
        list1 (List) - list of integers
    Return:
        the sum of the unique elements
    '''
    result = {}

    for i in list1:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    sam = 0
    for key, val in result.items():
        if val == 1:
            sam += key

    return sam

# Test cases
print(getUniques([1, 2, 3, 4, 5]))  # Expected Output: 15
print(getUniques([1, 2, 3, 2, 4]))  # Expected Output: 8
print(getUniques([1, 0, 2, 2, 2, 4, 6]))  # Expected Output: 11
