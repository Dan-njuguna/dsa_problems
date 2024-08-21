#!/usr/bin/python3
from typing import List


class Solution():
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width =  right - left
            area = width * min(height[left], height[right])

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


# Test cases
if __name__ == "__main__":
    obj = Solution()
    print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
    print(obj.maxArea([1, 1]))  # Output: 1
    print(obj.maxArea([4, 3, 2, 1, 4]))  # Output: 16
    print(obj.maxArea([1, 2, 1]))  # Output: 2