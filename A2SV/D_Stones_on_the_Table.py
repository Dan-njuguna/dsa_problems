def min_stones_to_remove(n, s):
    count = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    print(min_stones_to_remove(n, s))