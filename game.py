import random
import pygame
pygame.init()

from modules import board, cube
from modules.cube import Cube
from modules.snake import Snake
from settings import WHITE, BLACK, WIDTH, HEIGHT, FPS, GREY, RED, COOLDOWN, SQUARE_SIZE, WIN, TITLE, GAME_OVER_FONT, OTHER_FONT


pygame.display.set_caption(TITLE)



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
            if event.type == pygame.QUIT:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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


def draw_window(apple):
    WIN.fill(BLACK)
    board.draw_board(20, 20)
    pygame.draw.rect(WIN, RED, pygame.Rect(
        apple.x, apple.y, SQUARE_SIZE, SQUARE_SIZE))


def main():    
    snake = Snake([Cube(201,201,"down"), Cube(201, 176, "down"), Cube(201, 151, "down"), Cube(201, 126, "down")])
    apple = get_apple_position(snake.body)
    last = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            snake.movement(event)

        draw_window(apple)
        snake.draw()

        # check if snake's head and apple are on the same position
        if apple.x == snake.head.x and apple.y == snake.head.y:
            apple = get_apple_position(snake.body)
            butt = apple_eaten(snake.body)
            snake.body.append(butt)

        now = pygame.time.get_ticks()
        if now - last >= COOLDOWN:
            last = now
            snake.body_movement()
            did_bump_into_itself = snake.did_bump_into_itself()
            did_bump_into_border = snake.head_movement()
            if did_bump_into_border or did_bump_into_itself:
                game_over()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

