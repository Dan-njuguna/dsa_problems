#!/usr/bin/python3

def reconstructOriginalWord(n: int, s: str) -> str:
    current = []
    for c in reversed(s):
        pos = len(current) // 2
        current.insert(pos, c)
    return ''.join(current)


# Use Case
if __name__ == "__main__":
    l = int(input())
    word = input()
    print(reconstructOriginalWord(l, word))