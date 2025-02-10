def findNumber(n: int, t: int) -> int:
    # Smallest n-digit number
    smallest = 10 ** (n - 1)
    # Largest n-digit number
    largest = 10 ** n - 1

    # If smallest > largest, no such number exists
    if smallest > largest:
        return -1

    # Iterate through the range to find a number divisible by t
    for num in range(smallest, largest + 1):
        if num % t == 0:
            return num

    # If no number is found, return -1
    return -1

# Input
n, t = map(int, input().split())

# Output
result = findNumber(n, t)
print(result)