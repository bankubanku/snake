import pygame


def draw_board(surface, color, width, height, vFields, hFields):

    # vertical lines 
    i = width / vFields
    x = i
    while x < width:
        pygame.draw.rect(surface, color, pygame.Rect(x, 0, 1, 500))
        x += i
    # horizontal lines 
    i = height / hFields
    x = i
    while x < height:
        pygame.draw.rect(surface, color, pygame.Rect(0, x, 500, 1))
        x += i
