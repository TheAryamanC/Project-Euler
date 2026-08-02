"""
Project Euler - Problem 15: Lattice Paths

Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner. How many such routes are there through a $20 \times 20$ grid?
"""

import math

def solution():
    n = 20
    m = 20
    return math.comb(n + m, n)

if __name__ == "__main__":
    print(solution())  # Answer: 137846528820