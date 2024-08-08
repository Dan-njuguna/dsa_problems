#!/usr/bin/python3
from typing import List


class Solution():
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operations = [x.lower() for x in operations]
        x = 0
        for op in operations:
            if op == "x++" or op == "++x":
                x += 1
            elif op == "--x" or op == "x--":
                x -= 1
            else:
                raise ValueError(f"Invalid operation: {op}")
        return x


# Test
if __name__ == "__main__":
    sol = Solution()
    operations = ["--x", "x++", "x++"]  # Expected Output: 1
    print(sol.finalValueAfterOperations(operations))
    print(sol.finalValueAfterOperations(["x++", "++x", "--x", "x--"]))
    print(sol.finalValueAfterOperations(["x++", "++x", "--x", "X--"]))
