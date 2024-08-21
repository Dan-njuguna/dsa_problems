#!/usr/bin/python3
from typing import List


class Solution():
    def removeDuplicates(self, s: str) -> str:
        """You are given a string s consisting of lowercase English letters.
        A duplicate removal consists of choosing two adjacent and equal
        letters and removing them.

        Args:
            s (str): the given string
        
        Return:
            new string without duplicates
        """
        stack = []
        for item in s:
            if stack and stack[-1] == item:
                stack.pop()
            else:
                stack.append(item)
        
        return "".join(stack)
    

def main():
    s = Solution()
    print(s.removeDuplicates("abbaca"))
    print(s.removeDuplicates("aabbccde"))

main()