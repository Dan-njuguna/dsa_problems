#!/usr/bin/python3


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Initialize an array of size 26 to count character frequencies
        count_s = [0] * 26
        count_t = [0] * 26
        
        # Count frequencies of each character in both strings
        for char in s:
            count_s[ord(char) - ord('a')] += 1
        
        for char in t:
            count_t[ord(char) - ord('a')] += 1
        
        # Calculate the number of steps required
        steps = 0
        for i in range(26):
            if count_s[i] > count_t[i]:
                steps += count_s[i] - count_t[i]
        
        return steps


# Test Cases
if  __name__ == "__main__":
    solution = Solution()
    print(solution.minSteps(s = "bab", t = "aba"))  # Output: 1
    print(solution.minSteps(s = "leetcode", t = "practice"))  # Output: 5
