#!/usr/bin/python3
from typing import List


"""
Leetcode problem 2469: Convert the Temperature
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Level: Easy
Challenges: Basic mathematical operations
"""


# Solution 1: Using a single line of code
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    celcius = 36.50
    kelvin, fahrenheit = solution.convertTemperature(celcius)
    print(f"{celcius}°C is equal to {kelvin}°K and {fahrenheit}°F")
