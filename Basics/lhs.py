#!/usr/bin/python3
from typing import List


class Solution():
    def findLHS(self, nums: List[int]) -> int:
        '''Finds Longest Harmonious Subsequence and returns the length

        Args:
            nums (List): list of integers
        Return:
            count of longest harmonious subsequence
        
        A subsequence of array is a sequence that can be derived from the array
        by deleting some or no elements without charging the order of the
        remaining elements.
        '''
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        longest = 0
        for num in count:
            if num + 1 in count:
                longest = max(longest, count[num] + count[num + 1])
        
        return longest


# Test Case
if __name__ == "__main__":
    test = Solution()
    print(test.findLHS([1,3,2,2,5,2,3,7]))
    print(test.findLHS([1,2,3,4]))
    print(test.findLHS([1,1,1,1]))