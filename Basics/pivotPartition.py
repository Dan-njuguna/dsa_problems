#!/usr/bin/python3
from typing import List


class Solution():
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        equal = []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                equal.append(num)
        
        return left + equal + right


# Test case
if __name__ == "__main__":
    obj = Solution()
    print(obj.pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
    print(obj.pivotArray([3, 2, 1, 7, 1], 2))
    print(obj.pivotArray([1, 2, 3, 4, 5], 5))