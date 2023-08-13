import pygame

from modules.cube import Cube
from settings import WIN, GREEN, SQUARE_SIZE

class Snake:
    def __init__(self, body):
        self.body = body
        self.head = body[0]


    def movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and (self.head.direction == "right" or self.head.direction == "left"):
                self.head.direction = "up"
            if event.key == pygame.K_DOWN and (self.head.direction == "right" or self.head.direction == "left"):
                self.head.direction = "down"
            if event.key == pygame.K_RIGHT and (self.head.direction == "down" or self.head.direction == "up"):
                self.head.direction = "right"
            if event.key == pygame.K_LEFT and (self.head.direction == "down" or self.head.direction == "up"):
                self.head.direction = "left"


    def draw(self):
        for i in self.body:
            pygame.draw.rect(WIN, GREEN, pygame.Rect(
                i.x, i.y, SQUARE_SIZE, SQUARE_SIZE))


    '''
    Function handles snake's body movement

    # How it works?
    When head (on position 0) moves, 
    snake's part on position 1 inherits head's value, 
    part on positiion 2 inherits value of position 1 and so on
    '''
    def body_movement(self):
        for x in range(len(self.body)-1, 0, -1):
            self.body[x].x = self.body[x-1].x
            self.body[x].y = self.body[x-1].y
            self.body[x].direction = self.body[x-1].direction


    '''
    Function handles snake's head movement and reaching border

    # How it works?
    Function checks in which direction snake heads 
    and depently on that it changes its first part position.
    When snake reachs out of border, 
    then game_over()function is called 
    '''
    def head_movement(self):
        if self.head.direction == "up":
            self.head.y -= 25
            if self.head.y < 0:
                return True
        if self.head.direction == "down":
            self.head.y += 25
            if self.head.y >= 500:
                return True
        if self.head.direction == "right":
            self.head.x += 25
            if self.head.x >= 500:
                return True
        if self.head.direction == "left":
            self.head.x -= 25
            if self.head.x < 0:
                return True

        return False

    '''
    Function handles situation when snake bumps into itself

    # How it works?
    It checks if snake's head and any of other snake's part are on the same position.
    If so, game_over() function is called
    '''
    def did_bump_into_itself(self):
        for i in range(len(self.body)-1, 1, -1):
            if self.body[i].x == self.head.x and self.body[i].y == self.head.y:
                return True 