#!/usr/bin/python3
# Conways game of life in python
# Work in progress for fun
# Goal: Make the game of life as pythonic as possible
# @author: Stephen Greene


import argparse
import random
import time
from copy import copy, deepcopy
import os


DEAD_CELL = 0
LIVE_CELL = 1
REFRESH_RATE = .2


def main():
    parser = argparse.ArgumentParser(description="Conway's game of life")
    parser.add_argument('grid_size', type=int, help='side of square grid')
    size = int(parser.parse_args().grid_size)
    grid = [[random.getrandbits(1) for x in range(size)]
        for y in range(size)]
    while True:
        grid = turn(grid)
        for x in range(size):
            for y in range(size):
                if grid[x][y] == 1:
                    print("#", end='')
                else:
                    print(" ", end='')
            print()

        time.sleep(REFRESH_RATE)
        os.system('cls' if os.name == 'nt' else 'clear')


def turn(grid):
    # Deep copy to avoid pointer issues
    new_grid = deepcopy(grid)
    # Get frid size
    size = len(grid)
    for x in range(0, size):
        for y in range(0, size):
            neighbors = 0
            # Iterate over neighbors
            for a in range(-1, 2):
                for b in range(-1, 2):
                    # Boundary and neighbor checking
                    if ((x + a >= 0 and x + a < size) and (y + b >= 0 and
                        y + b < size) and (not(a == 0 and  b == 0))
                        and grid[x + a][y + b] == LIVE_CELL):
                        neighbors += 1

            # Rules of the game
            if grid[x][y] == LIVE_CELL:
                if neighbors < 2:
                    new_grid[x][y] = DEAD_CELL
                elif neighbors > 3:
                    new_grid[x][y] = DEAD_CELL
            elif grid[x][y] == DEAD_CELL and neighbors == 3:
                new_grid[x][y] = LIVE_CELL

    # Return the modified grid
    return new_grid


if __name__ == "__main__":
    main()
