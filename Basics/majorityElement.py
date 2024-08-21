#!/usr/bin/python3
from typing import List


class Solution():
    def majorityElement(self, nums: List[int]) -> int:
        els = {}
        
        for i in nums:
            if i in els:
                els[i] += 1
            else:
                els[i] = 1
        
        max_element = max(els, key = els.get)

        return max_element

# Test case
if __name__ == "__main__":
    test = Solution()
    print(test.majorityElement([3,2,3]))
    print(test.majorityElement([2,2,1,1,1,2,2]))