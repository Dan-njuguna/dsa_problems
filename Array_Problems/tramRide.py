#!/usr/bin/python3

'''Problem:
    https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/tram-ride-d7ff3a92/
'''
from typing import List


def solve(N: int, start: int, finish: int, Ticket_cost: List[int]) -> int:
    '''Function that finds the minimum cost given the distance
    Args:
        N: no. of Tram Stations
        start: start station
        finish: end station
        Ticket_cost: cost of each ticket
    Returns:
        res: The minimum cost

    _Example_
    Assumptions
        N = 4
        start = 1
        finish = 4
        ticket_cost = [1, 2, 2, 4 ]

    _Approach_
    path1 -> 1------1-----> 2 -------2------> 3 -------2------> 4 . =>
                                                            1+1+2+2 => 5

    path2 -> 1------4------>4 . => 4
    '''
    start -= 1
    finish -= 1

    # Calculate clockwise path cost
    if start <= finish:
        clockwise_cost = sum(Ticket_cost[start:finish])
    else:
        clockwise_cost = sum(Ticket_cost[start:]) + sum(Ticket_cost[:finish])

    # Calculate anticlockwise path cost
    if start >= finish:
        anticlockwise_cost = sum(Ticket_cost[finish:start])
    else:
        anticlockwise_cost = sum(Ticket_cost[finish:]) \
            + sum(Ticket_cost[:start])

    return min(anticlockwise_cost, clockwise_cost)


N = int(input())
start = int(input())
finish = int(input())
Ticket_cost = list(map(int, input().split()))

out_ = solve(N, start, finish, Ticket_cost)
print(out_)

'''Approach Explanation:

- The approach used is simply circulating through the array.
- The clockwise path will be from start to finish and the
    anticlockwise path will be from finish to start.
- Once both sums for both paths are checked, the minimum value of
    sum is taken to be the minimum transport cost.
- The time complexity of this solution is O(N) as it iterates
    through the array once.
- The space complexity is O(1) as it uses a constant amount of extra space.
'''
