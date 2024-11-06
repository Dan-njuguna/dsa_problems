#!/usr/bin/python3


def printFun(test: int):
    if test < 1:
        return

    else:
        print(test, end=" ")
        printFun(test - 1)
        print(test, end=" ")
        return 

test = 3
printFun(test)
