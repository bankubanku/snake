from modules.cube import Cube

class SnakesBody:
    def __init__(self, snake = [Cube(201,201,"down"), Cube(201, 176, "down"), Cube(201, 151, "down"), Cube(201, 126, "down")]):
        self.snake = snake
        self.head = snake[0]