# -*- coding: utf-8 -*-

import random
import curses
from itertools import chain

class Action(object):
    UP = 'up'
    LEFT = 'left'
    DOWN = 'down'
    RIGHT = 'right'
    RESTART = 'restart'
    EXIT = 'exit'

    letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
    actions = [UP, LEFT, DOWN, RIGHT, RESTART, EXIT]
    actions_dict = dict(zip(letter_codes, actions * 2))

    def __init__(self, stdscr):
        self.stdscr = stdscr
    
    def get(self):
        char = 'N'
        while char not in self.actions_dict:
            char = self.stdscr.getch()
            return self.actions_dict[char]

class Grid(object):
    
    def __init__(self, size):
        self.size = size
        self.cells = None
        self.reset()

    def reset(self):
        self.cells = [[0 for i in range(self.size)] for j in range(self.size)]
        self.add_randow_item()
        self.add_randow_item()
    
    def add_randow_item(self):
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.cells[i][j] == 0]
        (i, j) = random.choice(empty_cells)
        self.cells[i][j] = 4 if random.randrange(100) >= 90 else 2

    def transpose(self):
        return [list(row) for row in zip(*self.cells)]
    
    def invert(self):
        return [row[::-1] for row in self.cells]

    @staticmethod
    def move_left_row(row):
        def tighten(row):
            new_row = [i for i in row if i != 0]
            new_row += [0 for i in range(len(row) - len(new_row))]
            return new_row
        
        def merge(row):
            new_row = []
            pair = False
            for i in range(len(row)):
                if pair:
                    new_row.append(2 * row[i])
                    pair = False
                else:
                    if i + 1 < len(row) and row[i] == row[i + 1]:
                        pair = True
                        new_row.append(0)
                    else:
                        new_row.append(row[i])
            assert len(new_row) == len(row)
            return new_row
        return tighten(merge(tighten(row)))

    def move_left(self):
        self.cells = [self.move_left_row(row) for row in self.cells]
    
    def move_right(self):
        self.invert()
        self.move_left()
        self.invert()

    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()
    
    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    @staticmethod
    def row_can_move_left(row):
        def change(i):
            if row[i] == 0 and row[i + 1] != 0:
                return True
            if row[i] != 0 and row[i] == row[i + 1]:
                return True
            return False
        return any(change(i) for i in range(len(row) - 1))
    
    def row_can_move_right(self, row):
        self.invert()
        can = self.row_can_move_left(row)
        self.invert()
        return can
    
    def row_can_move_up(self, row):
        self.transpose()
        can = self.row_can_move_left(row)
        self.transpose()
        return can

    def row_can_move_down(self, row):
        self.transpose()
        can = self.row_can_move_right(row)
        self.transpose()
        return can


                
            

