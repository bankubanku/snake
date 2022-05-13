from re import X
import pygame

pygame.init()

FPS = 60
WIDTH, HEIGHT = 500, 500
BLACK = (0, 0, 0)
GREY = (96, 96, 96)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake by b4nq")


def draw_window():
    WIN.fill(BLACK)
    x = 25
    while x < 500:
        pygame.draw.rect(WIN, GREY, pygame.Rect(x, 0, 1, 500))
        x += 25
    x = 25
    while x < 500:
        pygame.draw.rect(WIN, GREY, pygame.Rect(0, x, 500, 1))
        x += 25
    
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
