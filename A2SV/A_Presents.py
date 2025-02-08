# Read input
n = int(input())
p = list(map(int, input().split()))

# Initialize the result list with zeros
result = [0] * n

# Fill the result list with the friend who gave the gift to each friend
for i in range(n):
    result[p[i] - 1] = i + 1

# Print the result
print(' '.join(map(str, result)))