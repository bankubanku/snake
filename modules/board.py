import pygame

from settings import WIN, GREY, WIDTH, HEIGHT, V_FIELDS, H_FIELDS

def draw_board(V_FIELDS, H_FIELDS):

    # vertical lines 
    i = WIDTH / V_FIELDS
    x = i
    while x < WIDTH:
        pygame.draw.rect(WIN, GREY, pygame.Rect(x, 0, 1, 500))
        x += i
    # horizontal lines 
    i = HEIGHT / H_FIELDS
    x = i
    while x < HEIGHT:
        pygame.draw.rect(WIN, GREY, pygame.Rect(0, x, 500, 1))
        x += i
