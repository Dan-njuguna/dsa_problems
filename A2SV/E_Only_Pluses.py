def max_bananas(a, b, c, operations):
    max_product = a * b * c
    for i in range(operations + 1):
        for j in range(operations + 1 - i):
            k = operations - i - j
            new_a = a + i
            new_b = b + j
            new_c = c + k
            max_product = max(max_product, new_a * new_b * new_c)
    return max_product

def main():
    t = int(input())
    results = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        results.append(max_bananas(a, b, c, 5))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()