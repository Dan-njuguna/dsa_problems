#!/usr/bin/python3
from typing import List


class NumArray:
    '''Prefix sum to calculate the sum of subarray in O(1)'''
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = []
        current = 0
        for  num in nums:
            current += num
            self.prefix_sum.append(current)


    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_sum[right]
        left_sum = self.prefix_sum[left - 1] if left > 0 else 0
        return right_sum - left_sum


# Test case
if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2))  # Output: 1
    print(obj.sumRange(2, 5))  # Output: -1
    print(obj.sumRange(0, 5))  # Output: -3