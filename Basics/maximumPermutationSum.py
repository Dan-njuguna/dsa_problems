#!/usr/bin/python3
from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
            n = len(nums)
            count = [0] * (n + 1)  # One extra space for the prefix sum trick
            
            # Step 1: Mark the start and end+1 of each request
            for start, end in requests:
                count[start] += 1
                if end + 1 < n:
                    count[end + 1] -= 1
            
            # Step 2: Calculate prefix sum to get the frequency of each index
            for i in range(1, n):
                count[i] += count[i - 1]
            
            # Step 3: Remove the extra space used for easier calculation
            count.pop()
            
            # Step 4: Sort the nums and count arrays to maximize the sum
            nums.sort(reverse = True)
            count.sort(reverse = True)
            
            # Step 5: Calculate the final answer
            return sum(a * b for a, b in zip(nums, count)) % (10**9 + 7)