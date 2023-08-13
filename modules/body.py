import pygame

from modules.cube import Cube
from settings import WIN, GREEN, SQUARE_SIZE

class SnakesBody:
    def __init__(self, body = [Cube(201,201,"down"), Cube(201, 176, "down"), Cube(201, 151, "down"), Cube(201, 126, "down")]):
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