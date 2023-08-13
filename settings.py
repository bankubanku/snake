import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (96, 96, 96)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# other
FPS = 60
WIDTH, HEIGHT = 500, 500
COOLDOWN = 200
SQUARE_SIZE = 24
GAME_OVER_FONT = pygame.font.SysFont('comicsans', 100)
OTHER_FONT = pygame.font.SysFont('comicsans', 20)
TITLE = 'snake by banku'
V_FIELDS = 20
H_FIELDS = 20

WIN = pygame.display.set_mode((WIDTH, HEIGHT))