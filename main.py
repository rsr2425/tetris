#
# Tetris
#

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

blue = (0, 128, 255)

pygame.draw.rect(screen, blue, pygame.Rect(30, 30, 60, 60))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
