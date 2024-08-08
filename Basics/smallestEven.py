#!/usr/bin/python3


class Solution():
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2


# Test
if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestEvenMultiple(6))
    print(solution.smallestEvenMultiple(5))
    print(solution.smallestEvenMultiple(10))
    print(solution.smallestEvenMultiple(15))
    print(solution.smallestEvenMultiple(18))
