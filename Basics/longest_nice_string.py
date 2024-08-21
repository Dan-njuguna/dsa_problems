#!/usr/bin/python3
from typing import List


class Solution():
    def longestNiceString(self, string: str) -> str:
        if not string or string[1:] == "":
            return ""
        
        idx = ""
        for i in range(len(string)):
            if string[i].lower() not in string or string[i].upper() not in string:
                left_part = self.longestNiceString(string[:i])
                right_part = self.longestNiceString(string[i+1:])
                return max(left_part, right_part, key=len)
        
        return string
    

# test case
if __name__ == "__main__":
    test = Solution()
    print(test.longestNiceString("YazaAay"))  # Pass the string directly
    print(test.longestNiceString("aBb"))
    print(test.longestNiceString("c"))
