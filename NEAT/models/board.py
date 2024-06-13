import pygame as pg # type: ignore

class Board():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        self.fps = 15
        self.bg_color = (0, 0, 0)

    def draw(self) -> None:
        self.screen.fill(self.bg_color)
        self.snake.draw(self)
        self.food.draw(self.screen)
        pg.display.flip()
        self.clock.tick(self.fps)

    def check_collision(self) -> None:
        self.snake.die(self)

    def check_eat(self) -> None:
        self.snake.eat(self.food)

    def move_snake(self) -> None:
        self.snake.move(self.snake.direction)

    def change_snake_direction(self, direction: str) -> None:
        self.snake.change_direction(direction)
