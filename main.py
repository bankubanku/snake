import pygame



WIDTH, HEIGHT = 500, 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake by b4nq")


def draw_window():
    WIN.fill(BLACK)
    for x in range(500):
        pygame.draw.rect(WIN, WHITE, pygame.Rect(x, 0, 5, 500))
    x += 50
    pygame.display.update()


def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
