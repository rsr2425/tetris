import random
from blocks import TTetro, BoxTetro, STetro, ZTetro
from main import GAME_BLOCK_UNIT, BLUE, WHITE, screen, x, y, score

__author__ = 'Ryan'


class BlockGrid(object):
    '''
    Stores the locations of all the blocks relevant to the game.  Also keeps
    track of how blocks interact, such as completing a row.

    The X specifies the upper left
    '''
    def __init__(self, X, Y, width, height):
        # initialize grid with available size
        # sqx - # of squares width-wise
        # sqy - # of squares height-wise
        self.sqx = width / GAME_BLOCK_UNIT
        self.sqy = height / GAME_BLOCK_UNIT
        self.grid = [[0 for i in range(self.sqx)] for j in range(self.sqy)]
        self.topleftx = X
        self.toplefty = Y
        self.drop()
        self.score = 0

    def draw(self):
        '''
        Draws all squares currently containted in the grid.
        '''

        # add falling falling block to grid
        # first check if there's no obstacle
        # otherwise backtrack
        obstacle = False
        for bx, by in self.fblock.get_grid_loc():
            if self.grid[by][bx] == 1:

                self.fblock.up()
                self.fblock.falling = False

        if self.fblock.falling:
            for bx, by in self.fblock.get_grid_loc():
                self.grid[by][bx] = 1


        # draw grid
        # (i, j)-th square in grid
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                if self.grid[j][i] == 1:
                    color = BLUE
                else:
                    color = WHITE
                pygame.draw.rect(screen, color, pygame.Rect(x + (i *
                                                               GAME_BLOCK_UNIT),
                                                               y + (j *
                                                               GAME_BLOCK_UNIT),
                                                               GAME_BLOCK_UNIT
                                                          , GAME_BLOCK_UNIT), 5)

        # remove falling block from grid
        if self.fblock.falling:
            for bx, by in self.fblock.get_grid_loc():
                self.grid[by][bx] = 0

    def drop(self, x=2, y=0):
        '''
        Adds a new falling block to the top line of the grid.
        '''
        choice = random.randint(1,4)
        if choice == 1:
            self.fblock = TTetro(x, y, self)
        elif choice == 2:
            self.fblock = BoxTetro(x, y, self)
        elif choice == 3:
            self.fblock = STetro(x, y, self)
        elif choice == 4:
            self.fblock = ZTetro(x, y, self)

    def update(self, input=None):
        '''
        Checks whether a move is valid, executes it, and sees if the
        move constitutes a special event.

        TODO Might be placing too much in this function.
        :param input:
        :return:
        '''
        if not self.fblock.falling:
            for bx, by in self.fblock.get_grid_loc():
                self.grid[by][bx] = 1
            self.drop()
        if input:
            self.fblock.move(input)

    # TODO still needs to remove the squares after row is complete and slide
    # down all of the squares
    def calc_score(self):
        for row in self.grid:
            if sum(row) == len(row):
                score(1)

    # TODO Remove when done with testing purposes
    def _complete_fst_row(self):
        for i in range(len(self.grid[0])):
            self.grid[0][i] = 1

