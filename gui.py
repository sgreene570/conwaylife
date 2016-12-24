# Game of life GUI
# @author Stephen Greene


import tkinter
import argparse
import random
import life
import time


def main():
    root = tkinter.Tk()
    parser = argparse.ArgumentParser(description="Conway's game of life")
    parser.add_argument('grid_size', type=int, help='side of square grid')
    size = int(parser.parse_args().grid_size)
    grid = [[random.getrandbits(1) for x in range(0, size)]
        for y in range(0, size)]
    while(True):
        for r in range(0, size):
            for c in range(0, size):
                tkinter.Label(
                root, text=str(grid[r][c]) + " ", borderwidth=1).grid(row=r,
                column=c)

        grid = life.turn(grid)
        root.update()
        time.sleep(.5)

    root.mainloop()


if __name__ == "__main__":
    main()
