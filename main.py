#
# Tetris
#
#


# set constants for script
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GAME_BLOCK_UNIT = 60

# Important Objects in the program
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
        # (i, j)-th square in grid
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                if self.grid[j][i] == 1:
                    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x + (i *
                                                               GAME_BLOCK_UNIT),
                                                               y + (j *
                                                               GAME_BLOCK_UNIT),
                                                               GAME_BLOCK_UNIT
                                                          , GAME_BLOCK_UNIT), 5)

    def drop(self, x=0, y=0):
        '''
        Adds a new falling block to the top line of the grid.
        '''
        self.grid[y][x] = 1
        self.fblock = (x, y)

    def update(self, input):
        '''
        Checks whether a move is valid, executes it, and sees if the
        move constitutes a special event.

        TODO Might be placing too much in this function.
        :param input:
        :return:
        '''
        if input == "DOWN":
            fx, fy = self.fblock
            self.grid[fy][fx] = 0
            self.grid[fy + 1][fx] = 1
            self.fblock = (fx, fy+1)
        elif input == "RIGHT":
            fx, fy = self.fblock
            self.grid[fy][fx] = 0
            self.grid[fy][fx + 1] = 1
            self.fblock = (fx+1, fy)
        elif input == "LEFT":
            fx, fy = self.fblock
            self.grid[fy][fx] = 0
            self.grid[fy][fx - 1] = 1
            self.fblock = (fx-1, fy)

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False
clock = pygame.time.Clock()

x = 100
y = 100

grid = BlockGrid(x, y, 600, 600)

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
