#!/usr/bin/env python
"""
 Tetris

 [Write desc. here]
"""

import random

import pygame
from blocks import TTetro, BoxTetro, STetro, ZTetro, LTetro, ITetro


BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

GAME_BLOCK_UNIT = 60

class BlockGrid(object):
    '''
    Stores the locations of all the blocks relevant to the game.  Also keeps
    track of how blocks interact, such as completing a row.

    (X,Y) specifies the upper left.
    '''
    def __init__(self, X, Y, width, height, s):
        # initialize grid with available size
        # sqx - # of squares width-wise
        # sqy - # of squares height-wise
        self.sqx = width / GAME_BLOCK_UNIT
        self.sqy = height / GAME_BLOCK_UNIT
        self.grid = [[0 for _ in range(self.sqx)] for _ in range(self.sqy)]
        self.topleftx = X
        self.toplefty = Y
        self.drop()
        # self.score = 0
        self.screen = s
        self.curr_score = 0

    def draw(self):
        '''
        Draws all squares currently containted in the grid.
        '''

        # add falling falling block to grid
        # first check if there's no obstacle
        # otherwise backtrack
        obstacle = False
        for BX, BY in self.fblock.get_grid_loc():
            if self.grid[BY][BX] == 1:
                self.fblock.backtrack()
                self.fblock.falling = False

        # add falling block to grid
        if self.fblock.falling:
            for BX, BY in self.fblock.get_grid_loc():
                self.grid[BY][BX] = 1


        # draw grid
        # (i, j)-th square in grid
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                if self.grid[j][i] == 1:
                    color = BLUE
                else:
                    color = WHITE
                pygame.draw.rect(self.screen, color, pygame.Rect(self.topleftx
                                                                 + (i *
                                                               GAME_BLOCK_UNIT),
                                                               self.toplefty
                                                                 + (j *
                                                               GAME_BLOCK_UNIT),
                                                               GAME_BLOCK_UNIT
                                                          , GAME_BLOCK_UNIT), 5)

        # remove falling block from grid
        if self.fblock.falling:
            for BX, BY in self.fblock.get_grid_loc():
                self.grid[BY][BX] = 0

    def drop(self, x=2, y=1):
        '''
        Adds a new falling block to the top line of the grid.
        '''
        choice = random.randint(1,6)
        if choice == 1:
            self.fblock = TTetro(x, y, self)
        elif choice == 2:
            self.fblock = BoxTetro(x, y, self)
        elif choice == 3:
            self.fblock = STetro(x, y, self)
        elif choice == 4:
            self.fblock = ZTetro(x, y, self)
        elif choice == 5:
            self.fblock = LTetro(x, y, self)
        elif choice == 6:
            self.fblock = ITetro(x, y, self)

    def update(self, input=None):
        '''
        Checks whether a move is valid, executes it, and sees if the
        move constitutes a special event.

        TODO Might be placing too much in this function.
        :param input:
        '''
        # check if block still falling
        # if not, permanently add to grid
        if not self.fblock.falling:
            for BX, BY in self.fblock.get_grid_loc():
                self.grid[BY][BX] = 1
            self.drop()
        self.calc_score()
        if input:
            self.fblock.move(input)

    def calc_score(self):
        """
        Add------------
        """
        for i in range(len(self.grid)):
            if sum(self.grid[i]) == len(self.grid[i]):
                self.curr_score += 1
                print "The current score is %s" % (self.curr_score)

                for j in range(len(self.grid[i])):
                    self.grid[i][j] = 0
                self.drop_grid(i)

    # Still seems a bit buggy
    # lrow - lowest row
    def drop_grid(self, lrow):
        """
        Add------------
        """
        # go backwards through the grid, starting at the bottom
        # and drop down blocks one row at a time
        n = len(self.grid[:lrow])
        for i in range(n):
            if i > 0:
                self.grid[n-i] = self.grid[n-1-i]
        map(lambda _ : 0, self.grid[0])