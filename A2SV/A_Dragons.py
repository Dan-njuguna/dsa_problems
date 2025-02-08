s, n = map(int, input().split())
dragons = []

for _ in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))

# Sort dragons by x ascending, and by y if x descending is equal
dragons.sort(key=lambda k: (k[0], -k[1]))

current = s
for x, y in dragons:
    if current > x:
        current += y
    else:
        print("NO")
        exit()

print("YES")
