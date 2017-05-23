#
# Tetris
#
#


# set constants for script
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GAME_BLOCK_UNIT = 60

# color constants
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Important Objects in the program
class Tetromino(object):
    def __init__(self, x=0, y=0):
        self.loc = x, y
        self.orient = 'u'

    def rotate_clockwise(self, curr_pos):
        raise NotImplemented()

    def down(self):
        # TODO Right now this could push it out of the grid
        fx, fy = self.loc
        self.loc = (fx, fy+1)

    def right(self):
        # TODO Right now this could push it out of the grid
        fx, fy = self.loc
        self.loc = (fx+1, fy)

    def left(self):
        fx, fy = self.loc
        self.loc = (fx-1, fy)

    def move(self, input):
        raise NotImplemented()

    def get_grid_loc(self):
        raise NotImplemented()


class BoxTetro(Tetromino):
    def move(self, input):
        if input == "DOWN":
            self.down()
        elif input == "RIGHT":
            self.right()
        elif input == "LEFT":
            self.left()

    def rotate_clockwise(self):
        pass

    # TODO need to include some kind of bounding checks
    def get_grid_loc(self):
        x, y = self.loc
        return [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]


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

    def draw(self):
        '''
        Draws all squares currently containted in the grid.
        '''

        # add falling falling block to grid
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
        for bx, by in self.fblock.get_grid_loc():
            self.grid[by][bx] = 0

    def drop(self, x=0, y=0):
        '''
        Adds a new falling block to the top line of the grid.
        '''
        self.fblock = BoxTetro(x,y)

    def update(self, input):
        '''
        Checks whether a move is valid, executes it, and sees if the
        move constitutes a special event.

        TODO Might be placing too much in this function.
        :param input:
        :return:
        '''
        self.fblock.move(input)

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False
clock = pygame.time.Clock()

x = 100
y = 100

grid = BlockGrid(x, y, 600, 600)
score = 0

# Main Game Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]: grid.update("DOWN")
    if pressed[pygame.K_LEFT]: grid.update("LEFT")
    if pressed[pygame.K_RIGHT]: grid.update("RIGHT")
    screen.fill((0,0,0))

    grid.draw()

    clock.tick(60)

    pygame.display.flip()
