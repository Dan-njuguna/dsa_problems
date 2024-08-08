#!/usr/bin/python3
from typing import List
from collections import Counter
"""
Problem: 1512. Number of Good Pairs
URL: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Author: David Wang
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return sum((v * (v - 1)) // 2 for v in count.values())


# Test Case
if __name__ == "__main__":
    solution = Solution()
    print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
    print(solution.numIdenticalPairs([1, 1, 1, 1]))
