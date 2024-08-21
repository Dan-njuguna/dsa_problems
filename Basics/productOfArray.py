#!/usr/bin/python3
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        left_product = 1
        right_product = 1

        # Step 1: Calculating the left products
        for i in range(n):
            answer[i] = left_product
            left_product = left_product * nums[i]
        
        # Step 2: Calculate right products and multiply with left products
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right_product
            right_product = right_product * nums[i]

        return answer


# Test cases
sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
print()