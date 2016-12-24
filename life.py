# Conways game of life in python
# Work in progress for fun
# Goal: Make the game of life as pythonic as possible
# @author: Stephen Greene


import argparse
import random
import time


DEAD_CELL = 0
LIVE_CELL = 1


def main():
    parser = argparse.ArgumentParser(description="Conway's game of life")
    parser.add_argument('grid_size', type=int, help='side of square grid')
    size = int(parser.parse_args().grid_size)
    grid = [[random.getrandbits(1) for x in range(size)]
        for y in range(size)]
    while True:
        turn(grid)
        for x in range(size):
            print(grid[x])
            print()
        time.sleep(1)


def turn(grid):
    size = len(grid)
    for x in range(size):
        for y in range(size):
            neighbors = 0;
            for a in range(-1, 2):       #Iterate through surrounding cells
                for b in range(-1, 2):
                    if (x + a >= 0 and x + a < size and y + b >= 0 and
                        y + b < size and grid[x + a][y + b] == LIVE_CELL
                        and (a != 0 or b != 0)):
                        neighbors += 1

            if neighbors < 2:
                grid[x][y] = DEAD_CELL
            elif neighbors == 3:
                grid[x][y] = LIVE_CELL
            elif neighbors > 3:
                grid[x][y] = DEAD_CELL

    return grid


if __name__ == "__main__":
    main()
