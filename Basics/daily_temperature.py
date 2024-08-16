#!/usr/bin/python3
from typing import List
'''QUESTION:
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible,
keep answer[i] == 0 instead.
'''


class Solution():
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Approach using LIFO(Stack)
        answer = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        # print(stack)  # For debugging purposes
        return answer
    

# Test Case
if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    print(solution.dailyTemperatures([30, 40, 50, 60]))  # Output: [1, 1, 1, 0]
    print(solution.dailyTemperatures([30, 60, 90]))  # Output: [1, 1, 0]