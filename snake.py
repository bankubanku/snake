import pygame
from modules import board, cube
import random
from modules.cube import Cube

pygame.init()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (96, 96, 96)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# settings
FPS = 60
WIDTH, HEIGHT = 500, 500
COOLDOWN = 250
SQUARE_SIZE = 24
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
GAME_OVER_FONT = pygame.font.SysFont('comicsans', 100)
OTHER_FONT = pygame.font.SysFont('comicsans', 20)
pygame.display.set_caption("Snake by b4nq")

'''
Function handles snake's head movement and reaching border

# How it works?
Function checks in which direction snake heads 
and depently on that it changes its first part position.
When snake reachs out of border, 
then game_over()function is called 
'''
def snakes_head_movement(snake):
    if snake[0].direction == "up":
        snake[0].y -= 25
        if snake[0].y < 0:
            print(2)
            game_over()
    if snake[0].direction == "down":
        snake[0].y += 25
        if snake[0].y >= 500:
            print(2)
            game_over()
    if snake[0].direction == "right":
        snake[0].x += 25
        if snake[0].x >= 500:
            print(2)
            game_over()
    if snake[0].direction == "left":
        snake[0].x -= 25
        if snake[0].x < 0:
            print(2)
            game_over()

'''
Function handles snake's body movement

# How it works?
When head (on position 0) moves, 
snake's part on position 1 inherits head's value, 
part on positiion 2 inherits value of position 1 and so on
'''
def snakes_body_movement(snake):
    for x in range(len(snake)-1, 0, -1):
        snake[x].x = snake[x-1].x
        snake[x].y = snake[x-1].y
        snake[x].direction = snake[x-1].direction



'''
Function handles situation when snake bumps into itself

# How it works?
It checks if snake's head and any of other snake's part are on the same position.
If so, game_over() function is called
'''
def does_bumped_into_itself(head, snake):
    for i in range(len(snake)-1, 1, -1):
        if snake[i].x == head.x and snake[i].y == head.y:
            print(1)
            game_over()

'''
Function returns position of snake's new part 
'''
def apple_eaten(snake):
    butt = None
    if snake[-1].direction == "down":
        butt = Cube(snake[-1].x, snake[-1].y, "down") #[snake[-1][0], snake[-1].y - 25, "down"]
    if snake[-1].direction == "up":
        butt = Cube(snake[-1].x, snake[-1].y + 25, "up")
    if snake[-1].direction == "right":
        butt = Cube(snake[-1].x + 25, snake[-1].y, "right")
    if snake[-1].direction == "left":
        butt = Cube(snake[-1].x - 25, snake[-1].y, "left")

    return butt


def get_apple_position(snake):
    pool = []

    for x in range(1, 476, 25):
        for y in range(1, 476, 25):
            pool.append(Cube(x, y))

    for i in range(len(snake)-1):
        for j in range(len(pool)-1):
            if snake[i] != pool[j]:
                continue
            else:
                pool.pop(j)

    apple = random.choice(pool)

    return apple

'''
Quit or restart options handler
'''
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

'''
Game over screen
'''
def game_over():
    drawGameOverText = GAME_OVER_FONT.render("Game Over", 1, WHITE)
    drawPlayAgainText = OTHER_FONT.render(
        "Press enter to play again", 1, WHITE)
    drawQuitText = OTHER_FONT.render("Press esc to quit", 1, WHITE)
    WIN.blit(drawGameOverText, (WIDTH/2 - drawGameOverText.get_width() /
             2, HEIGHT/2 - drawGameOverText.get_height()/2))
    WIN.blit(drawPlayAgainText, (WIDTH/2 - drawPlayAgainText.get_width() / 2,
             HEIGHT/2 - drawPlayAgainText.get_height()/2 - drawGameOverText.get_height()/2))
    WIN.blit(drawQuitText, (WIDTH/2 - drawQuitText.get_width() / 2, HEIGHT/2 - drawQuitText.get_height() /
             2 - drawPlayAgainText.get_height()/2 - drawGameOverText.get_height()/2 - 25))
    pygame.display.update()
    wait_for_key_press()


def draw_snake(snake):
    for i in snake:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(
            i.x, i.y, SQUARE_SIZE, SQUARE_SIZE))


def draw_window(apple):
    WIN.fill(BLACK)
    board.draw_board(WIN, GREY, WIDTH, HEIGHT, 20, 20)
    pygame.draw.rect(WIN, RED, pygame.Rect(
        apple.x, apple.y, SQUARE_SIZE, SQUARE_SIZE))


def main():    
    snake = [Cube(201,201,"down"), Cube(201, 176, "down"), Cube(201, 151, "down"), Cube(201, 126, "down")]
    apple = get_apple_position(snake)
    last = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and (snake[0].direction == "right" or snake[0].direction == "left"):
                    snake[0].direction = "up"
                if event.key == pygame.K_DOWN and (snake[0].direction == "right" or snake[0].direction == "left"):
                    snake[0].direction = "down"
                if event.key == pygame.K_RIGHT and (snake[0].direction == "down" or snake[0].direction == "up"):
                    snake[0].direction = "right"
                if event.key == pygame.K_LEFT and (snake[0].direction == "down" or snake[0].direction == "up"):
                    snake[0].direction = "left"

        draw_window(apple)
        draw_snake(snake)

        # check if snake's head and apple are on the same position
        if apple.x == snake[0].x and apple.y == snake[0].y:
            apple = get_apple_position(snake)
            butt = apple_eaten(snake)
            snake.append(butt)

        now = pygame.time.get_ticks()
        if now - last >= COOLDOWN:
            last = now
            snakes_body_movement(snake)
            does_bumped_into_itself(snake[0], snake)
            snakes_head_movement(snake)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

