#!/usr/bin/python3
from typing import List


class Solution():
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1  # Pointer for nums1
        j = n - 1  # Pointer for nums2
        k = m + n - 1  # Pointer for the merged array in nums1
        
        # Merge in reverse order to avoid overwriting elements in nums1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# Test Case
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution.merge(nums1, 3, nums2, 3)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
    print()
