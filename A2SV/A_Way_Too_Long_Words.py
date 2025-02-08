#!/usr/bin/python3

def wayTooLong(s: str):
    if len(s) <= 10:
        return s

    return f"{s[0]}{len(s)-2}{s[-1]}"            


# Usecase
if __name__ == "__main__":
    r = int(input())
    lines_list = []

    for i in range(r):
        line = input()
        lines_list.append(line)

    for j in range(r):
        print(wayTooLong(lines_list[j]))