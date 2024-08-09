#!/usr/bin/python3
from typing import List


class Solution():
    def isValid(self, s: str) -> bool:
        """Checks if the parantheses are of the same type

        Args:
            s (str): string of parantheses

        Returns:
            bool: True if valid, False otherwise

        Example:
            Input: s = "()"
            Output: True

            Input: s = "()[]{}"
            Output: True

            Input: s = "(]"
            Output: False
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s: # "()"
            if char in mapping.values():  # TODO: "(", is appended to stack list
                stack.append(char)
            elif char in mapping.keys(): #  TODO: ")", is appended to stack list
                if not stack or stack.pop() != mapping[char]: 
                    return False
                
        return not stack
    

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    s = "()"
    print(sol.isValid(s))  # Expected output: True
    s = "()[]{}"
    print(sol.isValid(s))  # Expected output: True
    s = "(]"
    print(sol.isValid(s))  # Expected output: False
    s = "([)]"
    print(sol.isValid(s))  # Expected output: False