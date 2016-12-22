# Conways game of life in python
# @author: Stephen Greene

import argparse
import random
import time


def main():
    parser = argparse.ArgumentParser(description="Conway's game of life")
    parser.add_argument('grid_size', type=int, help='side of square grid')
    size = int(parser.parse_args().grid_size)
    grid = [[random.getrandbits(1) for x in range(0, size)]
        for y in range(0, size)]
    while True:
        turn(grid)
        for x in range(0, size):
            print(grid[x])
            print()
        time.sleep(1)


def turn(grid):
    size = len(grid)
    for x in range(0, size):
        for y in range(0, size):
            neighbors = 0;
            for a in range(-1, 3, 2):       #Iterate through surrounding cells
                for b in range(-1, 3, 2):
                    if (x + a > 0 and x + a < size and y + b > 0 and
                        y + b < size and grid[x + a][y +b] == 1):
                        neighbors += 1

            if neighbors < 2:
                grid[x][y] = 0
            elif neighbors == 3:
                grid[x][y] = 1
            elif neighbors > 3:
                grid[x][y] = 0



if __name__ == "__main__":
    main()
