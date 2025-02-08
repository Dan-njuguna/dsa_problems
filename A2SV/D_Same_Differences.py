from typing import List

def same_differences(nums: List[int]) -> int:
    count = 0
    freq = {}
    
    for i, num in enumerate(lst):
        diff = num - i  # Calculate the key (num - index)
        if diff in freq:
            count += freq[diff]  # Add existing occurrences
        freq[diff] = freq.get(diff, 0) + 1  # Update frequency map

    return count


if __name__ == "__main__":
    t = int(input())  # Number of test cases
    
    while t > 0:
        n = int(input())  # Length of list
        lst = list(map(int, input().split()))  # Convert to list
        print(same_differences(lst))  # Call function and print result
        t -= 1