import pygame
import board

pygame.init()


class SnakesPart:
    def __init__(self, x, y):
        self.x = x
        self.y = y


COOLDOWN = 500
SQUARE_SIZE = 24
# colors
BLACK = (0, 0, 0)
GREY = (96, 96, 96)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# display settings
FPS = 60
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake by b4nq")


def draw_snake(snake):
    for i in snake:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(
            i.x, i.y, SQUARE_SIZE, SQUARE_SIZE))


def draw_window():
    WIN.fill(BLACK)
    board.draw_board(WIN, GREY, WIDTH, HEIGHT, 20, 20)


def main():
    snake = [SnakesPart(201, 201), SnakesPart(201, 176),
             SnakesPart(201, 151), SnakesPart(201, 126)]
    direction = "down"
    last = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and (direction == "right" or direction == "left"):
                    direction = "up"
                if event.key == pygame.K_DOWN and (direction == "right" or direction == "left"):
                    direction = "down"
                if event.key == pygame.K_RIGHT and (direction == "down" or direction == "up"):
                    direction = "right"
                if event.key == pygame.K_LEFT and (direction == "down" or direction == "up"):
                    direction = "left"

        now = pygame.time.get_ticks()
        if now - last >= COOLDOWN:
            last = now
            j = -1
            i = len(snake)
            '''Coś tu czasowo się pierdolneło'''
            while i > 1:
                j -= 1
                i -= 1
                snake[i] = snake[j]

            if direction == "up":
                snake[0].y -= 25
            if direction == "down":
                snake[0].y += 25
            if direction == "right":
                snake[0].x += 25
            if direction == "left":
                snake[0].x -= 25

            # j = 0
            # for i in reversed(snake):
            #     j -= 1
            #     i = snake[j]

        draw_window()
        draw_snake(snake)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

