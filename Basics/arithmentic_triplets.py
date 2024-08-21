#!/usr/bin/python3
from typing import List


class Solution():
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count += 1
        return count


# Test
if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 4, 6, 7, 10]
    diff = 3
    print(sol.arithmeticTriplets(nums, diff))  # Expected output: 2
    nums = [4, 5, 6, 7, 8, 9]
    diff = 2
    print(sol.arithmeticTriplets(nums, diff))  # Expected output: 2
