#
# Tetris
#
#

from grid import BlockGrid, SCREEN_WIDTH, SCREEN_HEIGHT, x, y, score

import pygame

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False
clock = pygame.time.Clock()

grid = BlockGrid(x, y, 600, 600, screen)
grid.grid[8][3] = 1

one_row_complete = False

# Main Game Loop
while not done:

    grid.update()

    # Temp code
    if grid.curr_score > 0:
        one_row_complete = True

    if not one_row_complete:
        grid.calc_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]: grid.update("DOWN")
    if pressed[pygame.K_LEFT]: grid.update("LEFT")
    if pressed[pygame.K_RIGHT]: grid.update("RIGHT")
    #if pressed[pygame.K_1]: grid.update("CLOCKW")
    #if pressed[pygame.K_2]: grid.update("COUNTERC")
    screen.fill((0,0,0))

    grid.draw()

    clock.tick(30)

    pygame.display.flip()
