#!/usr/bin/python3
from typing import List


class Solution():
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_string(string: str) -> str:
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return "".join(stack)
        
        return final_string(s) == final_string(t)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.backspaceCompare("ab#c", "ad#c")) # True
    print(solution.backspaceCompare("ab##", "c#d#")) # True
    print(solution.backspaceCompare("a##c", "#a#c")) # False
    print(solution.backspaceCompare("a#c", "b"))  # True
    print(solution.backspaceCompare("xywrrmp", "xywrrmu#p")) # True