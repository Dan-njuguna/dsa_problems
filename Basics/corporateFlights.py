#!/usr/bin/python3
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * (n + 1)
        
        for booking in bookings:
            first, last, seats = booking
            flights[first - 1] += seats
            if last < n:
                flights[last] -= seats
        
        for i in range(1, n):
            flights[i] += flights[i - 1]
        
        return flights[:-1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))