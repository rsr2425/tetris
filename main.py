#!/usr/bin/env python
"""
 Tetris

 [Write desc. here]

 [Specify nomenclature, like block grid.]
"""

from blocks import Directions as D
from grid import BlockGrid
import pygame
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False # pylint: disable=invalid-name
CLOCK = pygame.time.Clock()

# Specify top-left corner of block grid and size
GRID_X = 100
GRID_Y = 100
GRID_W = 600
GRID_H = 600


GRID = BlockGrid(GRID_X, GRID_Y, GRID_W, GRID_H, SCREEN)

# TESTING - initialize some blocks on grid
# GRID.grid[8][3] = 1

# Main Game Loop
while not done:

    GRID.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    PRESSED = pygame.key.get_pressed()
    if PRESSED[pygame.K_s]:
        GRID.update(D.DOWN)
    if PRESSED[pygame.K_a]:
        GRID.update(D.LEFT)
    if PRESSED[pygame.K_d]:
        GRID.update(D.RIGHT)
    if PRESSED[pygame.K_e ]:
        GRID.update(D.CLOCKWISE)
    if PRESSED[pygame.K_q]:
        GRID.update(D.COUNTERCLOCKWISE)

    # testing buttons
    if PRESSED[pygame.K_d]:
        GRID.drop_grid(GRID.sqy)
    SCREEN.fill((0, 0, 0))

    GRID.draw()

    CLOCK.tick(10)

    pygame.display.flip()
