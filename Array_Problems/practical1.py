#!/usr/bin/python3
from typing import List


# PEP8 Python Rules
# def fibonacci(lsr: List[int]) -> List[int]:  # a parameter
#     '''Calculates cumulative sum for a list.

#     Args:
#         lsr (list) - list of integers

#     Return:
#         List of cumulative sum.
#     '''
#     stack = []
#     sum = 0
#     for i in range(len(lsr)):
#         sum += lsr[i]
#         stack.append(sum)

#     return stack


# res = fibonacci([1, 2, 3, 4, 5, 6])  # An argument
# print(res)
# # [1, 3, 6, 10]

def fibonnaci_Recursion(lsr: List[int]) -> List[int]:
    '''Calculates cumulative sum for a list using recursion.

    Args:
        lsr (list) - list of integers

    Return:
        List of cumulative sum.
    '''
    if len(lsr) == 0:
        return []
    elif len(lsr) == 1:
        return [lsr[0]]
    else:
        return [lsr[0]] + fibonnaci_Recursion(lsr[1:])
    

print(fibonnaci_Recursion([1, 2, 3, 4, 5, 6]))