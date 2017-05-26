#!/usr/bin/env python
"""
 Tetris

 [Write desc. here]
"""

from grid import BlockGrid, X, Y


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

import pygame

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False # pylint: disable=invalid-name
CLOCK = pygame.time.Clock()

GRID = BlockGrid(X, Y, 600, 600, SCREEN)

# TESTING - initialize some blocks on grid
# GRID.grid[8][3] = 1

# Main Game Loop
while not done:

    GRID.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    PRESSED = pygame.key.get_pressed()
    if PRESSED[pygame.K_DOWN]:
        GRID.update("DOWN")
    if PRESSED[pygame.K_LEFT]:
        GRID.update("LEFT")
    if PRESSED[pygame.K_RIGHT]:
        GRID.update("RIGHT")

    # testing buttons
    if PRESSED[pygame.K_d]:
        GRID.drop_grid(GRID.sqy)
    SCREEN.fill((0, 0, 0))

    GRID.draw()

    CLOCK.tick(10)

    pygame.display.flip()
