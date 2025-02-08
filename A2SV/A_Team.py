# Read the number of problems
n = int(input())

# Initialize a counter for the problems to be solved
solvable_count = 0

# Process each problem
for _ in range(n):
    # Read three integers and sum them up
    sure_count = sum(map(int, input().split()))
    
    # If at least two friends are sure, count the problem as solvable
    if sure_count >= 2:
        solvable_count += 1

# Print the final count of solvable problems
print(solvable_count)
