#!/usr/bin/python3
from typing import List


class Solution():
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        '''Finds a 0-indexed integer array answer where:
                - answer.length == nums.length
                - answer[i] = |leftSum[i] - rightSum[i]|
            Where:
                - leftSum[i] is the sum of elements to the left of the index i
                in the array nums. If there is no such element, leftSum[i] = 0.
                - rightSum[i] is the sum of elements to the right of the index
                i in the array nums. If there is no such element, rightSum[i]=0
        Args:
            nums -> (List[int]): list of integers
        Return:
            a list of the differences.
        '''
        left_sum = 0
        total_sum = sum(nums)
        answer = []

        for num in nums:
            right_sum = total_sum - left_sum - num
            answer.append(abs(left_sum - right_sum))
            left_sum += num
        
        return answer


# Test Case
if __name__ == "__main__":
    test = Solution()
    print(test.leftRightDifference([10,4,8,3]))
    print(test.leftRightDifference([1]))