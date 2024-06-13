import pygame as pg # type: ignore
import numpy as np

import snake as sn
import food as fd

class State():
    def __init__(self, generation):
        self.generation = generation
        self.board.create_snake(200, 200)
        self.board.create_food(100, 100)
        self.score = 0

    def create_snake(self, x: int, y: int) -> None:
        self.snake = sn.Snake(x, y)

    def create_food(self, x: int, y: int) -> None:
        self.food = fd.Food(x, y)