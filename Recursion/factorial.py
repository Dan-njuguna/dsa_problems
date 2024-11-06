#!/usr/bin/python3


def factorial(num: int) -> int:
    '''Calculate factorial product of a number. Direct recursive Function.

    Args:
        nums (int) - the number to get factorial of.

    Return:
        Factorial product(int)
    '''
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


# Test Case
if __name__ == "__main__":
    print(factorial(5))
    print(factorial(-5))
    print(factorial(0))
    print(factorial(11))
