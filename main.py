import pygame
import board
import random

pygame.init()


class SnakesPart:
    def __init__(self, x, y):
        self.x = x
        self.y = y


COOLDOWN = 500
SQUARE_SIZE = 24
GAME_OVER_FONT = pygame.font.SysFont('comicsans', 100)
OTHER_FONT = pygame.font.SysFont('comicsans', 20)
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (96, 96, 96)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# display settings
FPS = 60
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake by b4nq")

def wait_for_key_press():
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    wait = False
                    pygame.quit()
                elif event.key == pygame.K_RETURN:
                    main()

def gameOver():
    drawGameOverText = GAME_OVER_FONT.render("Game Over", 1, WHITE)
    drawPlayAgainText = OTHER_FONT.render("Press enter to play again", 1, WHITE)
    drawQuitText = OTHER_FONT.render("Press esc to quit", 1, WHITE)
    WIN.blit(drawGameOverText, (WIDTH/2 - drawGameOverText.get_width() / 2, HEIGHT/2 - drawGameOverText.get_height()/2))
    WIN.blit(drawPlayAgainText, (WIDTH/2 - drawPlayAgainText.get_width() / 2, HEIGHT/2 - drawPlayAgainText.get_height()/2 - drawGameOverText.get_height()/2))
    WIN.blit(drawQuitText, (WIDTH/2 - drawQuitText.get_width() / 2, HEIGHT/2 - drawQuitText.get_height()/2  - drawPlayAgainText.get_height()/2 - drawGameOverText.get_height()/2 - 25))
    pygame.display.update()
    wait_for_key_press()
    #pygame.time.delay(5000)


        

def draw_snake(snake):
    for i in snake:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(
            i[0], i[1], SQUARE_SIZE, SQUARE_SIZE))


def draw_window():
    WIN.fill(BLACK)
    board.draw_board(WIN, GREY, WIDTH, HEIGHT, 20, 20)


def main():
    #snake = [SnakesPart(201, 201), SnakesPart(201, 176),
    #         SnakesPart(201, 151), SnakesPart(201, 126)]
    snake = [[201,201],[201,176],[201,151],[201,126]]
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

        draw_window()
        draw_snake(snake)

        now = pygame.time.get_ticks()
        if now - last >= COOLDOWN:
            last = now

            for x in range(len(snake)-1,0,-1):
                snake[x][0] = snake[x-1][0]
                snake[x][1] = snake[x-1][1]
            
                
            if direction == "up":
                snake[0][1] -= 25
                if snake[0][1] < 0:
                    gameOver()
            if direction == "down":
                snake[0][1] += 25
                if snake[0][1] >= 500:
                    gameOver()
            if direction == "right":
                snake[0][0] += 25
                if snake[0][0] >= 500:
                    gameOver()
            if direction == "left":
                snake[0][0] -= 25
                if snake[0][0] < 0:
                    gameOver()

            
        
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
