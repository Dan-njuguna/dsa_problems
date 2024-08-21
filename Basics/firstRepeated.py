#!/usr/bin/python3
from typing import List


class Solution():
    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for c in s:
            if c in seen:
                return c
            seen.add(c)
        return ""


# Test Cases
if __name__ == "__main__":
    test = Solution()
    print(test.repeatedCharacter("abccbaacz"))