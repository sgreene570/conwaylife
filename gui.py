# Game of life GUI
# @author Stephen Greene


import tkinter
import argparse
import random
import life
import time


def main():
    parser = argparse.ArgumentParser(description="Conway's game of life")
    parser.add_argument('grid_size', type=int, help='side of square grid')
    size = int(parser.parse_args().grid_size)
    grid = [[random.getrandbits(1) for x in range(size)]
        for y in range(size)]
    b = tkinter.Button(root, text="Turn", command=output_grid(grid = life.turn(grid))).grid(row = size, column = size)
    output_grid(grid)
    root.mainloop()


def output_grid(grid):
    size = len(grid)
    for r in range(size):
        for c in range(size):
            if(grid[r][c] == life.DEAD_CELL):
                tkinter.Label(root, text="   ", bg='black', borderwidth = 1).grid(row = r, column = c)
            elif(grid[r][c] == life.LIVE_CELL):
                tkinter.Label(root, text="   ", bg='white', borderwidth = 1).grid(row = r, column = c)

    root.update()


if __name__ == "__main__":
    root = tkinter.Tk()
    main()
