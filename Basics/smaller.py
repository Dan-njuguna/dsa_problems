#!/usr/bin/python3
from typing import List


class Solution():
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        rank = {}
        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i
        
        return [rank[num] for num in nums]


# Test Case
if __name__ == "__main__":
    test = Solution()
    print(test.smallerNumbersThanCurrent([8,1,2,2,3]))  # Output: [4, 0, 1, 1, 3]