import pygame
from modules import board, cube
import random
from modules.cube import Cube
from modules.body import SnakesBody

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
def snakes_head_movement(head):
    if head.direction == "up":
        head.y -= 25
        if head.y < 0:
            print(2)
            game_over()
    if head.direction == "down":
        head.y += 25
        if head.y >= 500:
            print(2)
            game_over()
    if head.direction == "right":
        head.x += 25
        if head.x >= 500:
            print(2)
            game_over()
    if head.direction == "left":
        head.x -= 25
        if head.x < 0:
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
        butt = Cube(snake[-1].x, snake[-1].y, "down") 
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
    body = SnakesBody()
    apple = get_apple_position(body.snake)
    last = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and (body.head.direction == "right" or body.head.direction == "left"):
                    body.head.direction = "up"
                if event.key == pygame.K_DOWN and (body.head.direction == "right" or body.head.direction == "left"):
                    body.head.direction = "down"
                if event.key == pygame.K_RIGHT and (body.head.direction == "down" or body.head.direction == "up"):
                    body.head.direction = "right"
                if event.key == pygame.K_LEFT and (body.head.direction == "down" or body.head.direction == "up"):
                    body.head.direction = "left"

        draw_window(apple)
        draw_snake(body.snake)

        # check if snake's head and apple are on the same position
        if apple.x == body.head.x and apple.y == body.head.y:
            apple = get_apple_position(body.snake)
            butt = apple_eaten(body.snake)
            body.snake.append(butt)

        now = pygame.time.get_ticks()
        if now - last >= COOLDOWN:
            last = now
            snakes_body_movement(body.snake)
            does_bumped_into_itself(body.head, body.snake)
            snakes_head_movement(body.head)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

