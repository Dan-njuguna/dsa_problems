#!/usr/bin/python3

strs = input()

upper = 0
lower = 0

for i in strs:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

if upper > lower:
    print(strs.upper())
else:
    print(strs.lower())