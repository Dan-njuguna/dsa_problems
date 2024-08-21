#!/usr/bin/python3
from typing import List


class Solution():
    def runningSum(self, nums: List[int]) -> List[int]:
        """Calculate the running sum of a list of integers.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: A list of running sums.

        Examples:
            >>> test = Solution()
            >>> test.runningSum([1,2,3,4])
            [1, 3, 6, 10]
            >>> test.runningSum([1,1,1,1,1])
            [1, 2, 3, 4, 5]
            >>> test.runningSum([3,1,2,10,1])
            [3, 4, 6, 16, 17]
        """
        run = []
        sm = 0
        for i in nums:
            sm += i
            run.append(sm)
        return run


# Test Cases
if __name__ == "__main__":
    test = Solution()
    print(test.runningSum([1,2,3,4]))
    print(test.runningSum([1,1,1,1,1]))
    print(test.runningSum([3,1,2,10,1]))