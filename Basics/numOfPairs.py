#!/usr/bin/python3
from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        

        for  i in range(len(nums)):
            prefix = target[:len(nums[i])]
            suffix = target[len(nums[i]):]

            if prefix == nums[i] and suffix in freq:
                count += freq[suffix]
                if suffix == nums[i]:
                    count -= 1
        
        return count


# Test the Object
if __name__ == "__main__":
    solution = Solution()
    print(solution.numOfPairs(nums = ["777","7","77","77"], target = "7777"))  #  Output: 4
    print(solution.numOfPairs(nums = ["123","4","12","34"], target = "1234"))  # Output: 2
    print(solution.numOfPairs(nums = ["1","1","1"], target = "11"))  # Output: 6
    print(solution.numOfPairs(nums = ["1", "1", "1"], target = "1"))  # Output: 0
    print(solution.numOfPairs(nums = ["1", "111"], target = "11"))  # Output: 0
