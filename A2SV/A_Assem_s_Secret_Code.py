#!/usr/bin/python3

def secretCode(s: str) -> str:
    if s.upper() == "YES":
        return "YES"
    else:
        return "NO"

# Use case
if __name__ == "__main__":
    t = int(input())

    while t > 0:
        s = input()
        print(secretCode(s))
        t -= 1