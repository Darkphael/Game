import pygame
x_position=0
y_position=0
def animation():
    global x_position, y_position
    if pressed[pygame.K_UP]:
        y_position = 0
    elif pressed[pygame.K_DOWN]:
        y_position = 32
    elif pressed[pygame.K_LEFT]:
        x_position += 32
    elif pressed[pygame.K_RIGHT]:
        x_position += 32
