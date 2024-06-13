import pygame as pg # type: ignore

class Snake():
    def __init__(self, x: int, y: int, life: int, color) -> None:
        self.x = x
        self.y = y
        self.body = [(x, y)]
        self.cell = 10
        self.color = color
        self.direction = 'n'
        self.score = 0
        self.alive = True
        self.steps = 0
        self.life = life

    def draw(self, screen) -> None:
       
        for x, y in self.body:
            pg.draw.rect(screen, self.color, (x, y, self.cell, self.cell))
        
    def change_direction(self, direction: str) -> None:
        if direction == 'n' and self.direction != 's':
            self.direction = 'n'
        elif direction == 's' and self.direction != 'n':
            self.direction = 's'
        elif direction == 'w' and self.direction != 'e':
            self.direction = 'w'
        elif direction == 'e' and self.direction != 'w':
            self.direction = 'e'
            
    def grow(self) -> None:
        self.body.append(self.body[-1])
        
    def check_collision(self, width, height) -> bool:
        if self.x < 0 or self.x >= width or self.y < 0 or self.y >= height:
            return True
        if len(self.body) != len(set(self.body)):
            return True
        return False
    
    def die(self, width, height) -> None:
        if(self.check_collision(width, height)):
            self.alive = False
            self.body = [(0, 0)]
            self.x = 0
            self.y = 0
            self.direction = 'n'
        return not self.alive
    
    def eat (self, food) -> None:
        if self.x == food.x and self.y == food.y:
            self.grow()
        
    def move(self) -> None:
        direction = self.direction
        if direction == 'n':
            self.y -= self.cell
        elif direction == 's':
            self.y += self.cell
        elif direction == 'w':
            self.x -= self.cell
        elif direction == 'e':
            self.x += self.cell
        self.body.insert(0, (self.x, self.y))
        self.body.pop()
        
    def take_inputs(self, food, width, height) -> list:
        out = [
            0, 0, 0, # if food is in front, left or right
            0, 0, 0, # if the snake can move forward, left or right (no wall)
            0, 0, 0 # if the snake can move to the left, right or forward (no body part)
            #5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, # distance to food in 8 directions
        ]
        
        # check if food is in the front
        if self.direction == 'n' and self.y > food.y and self.x == food.x:
            out[0] = 1
        elif self.direction == 's' and self.y < food.y and self.x == food.x:
            out[0] = 1
        elif self.direction == 'w' and self.x > food.x and self.y == food.y:
            out[0] = 1
        elif self.direction == 'e' and self.x < food.x and self.y == food.y:
            out[0] = 1
            
        # check if food is to the left
        if self.direction == 'n' and self.x > food.x and self.y == food.y:
            out[1] = 1
        elif self.direction == 's' and self.x < food.x and self.y == food.y:
            out[1] = 1
        elif self.direction == 'w' and self.y < food.y and self.x == food.x:
            out[1] = 1
        elif self.direction == 'e' and self.y > food.y and self.x == food.x:
            out[1] = 1
            
        # check if food is to the right
        if self.direction == 'n' and self.x < food.x and self.y == food.y:
            out[2] = 1
        elif self.direction == 's' and self.x > food.x and self.y == food.y:
            out[2] = 1
        elif self.direction == 'w' and self.y > food.y and self.x == food.x:
            out[2] = 1
        elif self.direction == 'e' and self.y < food.y and self.x == food.x:
            out[2] = 1
            
        # check if the snake can move forward (no wall in front)
        if self.direction == 'n' and self.y - self.cell >= 0:
            out[3] = 1
        elif self.direction == 's' and self.y + self.cell < height:
            out[3] = 1
        elif self.direction == 'w' and self.x - self.cell >= 0:
            out[3] = 1
        elif self.direction == 'e' and self.x + self.cell < width:
            out[3] = 1
        
        # check if the snake can move forward (no body part in front)
        if self.direction == 'n' and (self.x, self.y - self.cell) not in self.body:
            out[6] = 1
        elif self.direction == 's' and (self.x, self.y + self.cell) not in self.body:
            out[6] = 1
        elif self.direction == 'w' and (self.x - self.cell, self.y) not in self.body:
            out[6] = 1
        elif self.direction == 'e' and (self.x + self.cell, self.y) not in self.body:
            out[6] = 1
            
        # check if the snake can move to the left (no wall to the left)
        if self.direction == 'n' and self.x - self.cell >= 0:
            out[4] = 1
        elif self.direction == 's' and self.x + self.cell < width:
            out[4] = 1
        elif self.direction == 'w' and self.y + self.cell < height:
            out[4] = 1
        elif self.direction == 'e' and self.y - self.cell >= 0:
            out[4] = 1
            
        # check if the snake can move to the left (no body part to the left)
        if self.direction == 'n' and (self.x - self.cell, self.y) not in self.body:
            out[7] = 1
        elif self.direction == 's' and (self.x + self.cell, self.y) not in self.body:
            out[7] = 1
        elif self.direction == 'w' and (self.x, self.y + self.cell) not in self.body:
            out[7] = 1
        elif self.direction == 'e' and (self.x, self.y - self.cell) not in self.body:
            out[7] = 1
            
        # check if the snake can move to the right (no wall to the right)
        if self.direction == 'n' and self.x + self.cell < width:
            out[5] = 1
        elif self.direction == 's' and self.x - self.cell >= 0:
            out[5] = 1
        elif self.direction == 'w' and self.y - self.cell >= 0:
            out[5] = 1
        elif self.direction == 'e' and self.y + self.cell < height:
            out[5] = 1
            
        # check if the snake can move to the right (no body part to the right)
        if self.direction == 'n' and (self.x + self.cell, self.y) not in self.body:
            out[8] = 1
        elif self.direction == 's' and (self.x - self.cell, self.y) not in self.body:
            out[8] = 1
        elif self.direction == 'w' and (self.x, self.y - self.cell) not in self.body:
            out[8] = 1
        elif self.direction == 'e' and (self.x, self.y + self.cell) not in self.body:
            out[8] = 1
            
        return out
