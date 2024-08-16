#!/usr/bin/python3
import os
from typing import List
"""QUESTION:

You are keeping the scores for a baseball game with strange rules.
At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i]
is the ith operation you must apply to the record and is one of the following:

    An integer x.
    Record a new score of x.
    '+'.
    Record a new score that is the sum of the previous two scores.
    'D'.
    Record a new score that is the double of the previous score.
    'C'.
    Invalidate the previous score, removing it from the record.
        Return the sum of all the scores on the record after applying
        all the operations
"""


class Solution():
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                if len(record) >= 2:
                    record.append(record[-1] + record[-2])
            elif op == 'D':
                if record:
                    record.append(record[-1] * 2)
            elif op == 'C':
                if record:
                    record.pop()
            else:
                if op.isdigit():
                    record.append(int(op))

        return sum(record)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.calPoints(["5", "2", "C", "D", "+"]))
    print(solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
    print(solution.calPoints(["1"]))
    print(solution.calPoints(["10", "2", "D", "X"]))
