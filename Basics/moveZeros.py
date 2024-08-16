#!/usr/bin/python3
from typing import List


class Solution():
    def moveZeros(self, nums: List[int]) -> None:
        last_non_zero_index = 0

        # Take all non-zero values in the list in their original order.
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1
        
        # Add the remaining values of zero values to the list.
        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0
        
        print(nums)

# Test Case
if __name__ == "__main__":
    test = Solution()
    test.moveZeros([0,1,0,3,12])
    test.moveZeros([1, 0, 2, 3, 0, 6, 0, 7])
