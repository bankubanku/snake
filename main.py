import pygame
import board

pygame.init()

# colors
BLACK = (0, 0, 0)
GREY = (96, 96, 96)
RED = (255, 0, 0)
# display settings 
FPS = 60
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake by b4nq")


def draw_window():
    WIN.fill(BLACK)
    board.draw_board(WIN, GREY, WIDTH, HEIGHT, 20, 20)
    pygame.draw.rect(WIN, RED, pygame.Rect(26, 26, 24, 24))
    pygame.display.update()


def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
