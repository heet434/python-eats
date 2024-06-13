import pygame as pg # type: ignore

# define color of food
red = (255, 0, 0)

class Food():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.size = 10
        self.color = red

    def draw(self, screen) -> None:
        pg.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))