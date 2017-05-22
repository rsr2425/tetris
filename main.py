#
# Tetris
#
#

# Helper Functions
def draw_box(x, y):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, GAME_BLOCK_UNIT
                                                , GAME_BLOCK_UNIT), 5)
    pygame.draw.rect(screen, color, pygame.Rect(x+GAME_BLOCK_UNIT, y,
                                                GAME_BLOCK_UNIT,
                                                GAME_BLOCK_UNIT), 5)
    pygame.draw.rect(screen, color, pygame.Rect(x, y+GAME_BLOCK_UNIT,
                                                GAME_BLOCK_UNIT,
                                                GAME_BLOCK_UNIT), 5)
    pygame.draw.rect(screen, color, pygame.Rect(x+GAME_BLOCK_UNIT,
                                                y+GAME_BLOCK_UNIT,
                                                GAME_BLOCK_UNIT,
                                                GAME_BLOCK_UNIT), 5)

def draw_T(x, y):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, GAME_BLOCK_UNIT
                                                , GAME_BLOCK_UNIT), 5)
    pygame.draw.rect(screen, color, pygame.Rect(x+GAME_BLOCK_UNIT, y,
                                                GAME_BLOCK_UNIT,
                                                GAME_BLOCK_UNIT), 5)
    pygame.draw.rect(screen, color, pygame.Rect(x, y+GAME_BLOCK_UNIT,
                                                GAME_BLOCK_UNIT,
                                                GAME_BLOCK_UNIT), 5)
    pygame.draw.rect(screen, color, pygame.Rect(x-GAME_BLOCK_UNIT,
                                                y,GAME_BLOCK_UNIT,
                                                GAME_BLOCK_UNIT), 5)

import pygame
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_BLOCK_UNIT = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False
clock = pygame.time.Clock()


blue = (0, 128, 255)
is_blue = True

x = GAME_BLOCK_UNIT
y = GAME_BLOCK_UNIT

# Main Game Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    # Adjust falling block according to user input
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= GAME_BLOCK_UNIT
    if pressed[pygame.K_DOWN]: y += GAME_BLOCK_UNIT
    if pressed[pygame.K_LEFT]: x -= GAME_BLOCK_UNIT
    if pressed[pygame.K_RIGHT]: x += GAME_BLOCK_UNIT

    y += 1
    screen.fill((0,0,0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    draw_T(x,y)

    clock.tick(60)

    pygame.display.flip()
