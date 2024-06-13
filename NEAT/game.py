import pygame # type: ignore
import time
import random
import neat 
import os

random.seed(434)

import models.snake as sn
import models.food as fd

snake_speed = 20


window_x = 300
window_y = 300

life = 200

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()


pygame.display.set_caption('Snakes')
screen = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

def show_score(choice, color, font, size, score):

	score_font = pygame.font.SysFont(font, size)
	score_surface = score_font.render('Max Score : ' + str(score), True, color)
	score_rect = score_surface.get_rect()
	screen.blit(score_surface, score_rect)

def game_over(score):

	my_font = pygame.font.SysFont('times new roman', 50)
	game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
	game_over_rect = game_over_surface.get_rect()
	game_over_rect.midtop = (window_x/2, window_y/4)
	screen.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	time.sleep(2)
	pygame.quit()
	quit()

generation_count = 0
 
def eval_genomes(genomes, config):
    
    # display snake generation on top
    global generation_count
    pygame.display.set_caption('Generation : ' + str(generation_count))
    
    fruits = []
    snakes = []
    nets = []
    ge = []

    # initialize snakes with different shades of light green
    bright_colors = [(0, 255, 0), (0, 200, 0), (0, 150, 0), (0, 100, 0), (0, 50, 0)]
    
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)

        snake = sn.Snake(random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10, life, random.choice(bright_colors))
        snakes.append(snake)
        fruit = fd.Food(random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10)
        fruits.append(fruit)
        g.fitness = 0
        ge.append(g)

    max_score = 0
    Run = True
    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        for x, snake in enumerate(snakes):
            
            snake.steps += 1
            snake.move()
            
            inputs = snake.take_inputs(fruits[x], window_x, window_y)
            
            output = nets[x].activate(inputs)
            
            if(output[0] == max(output)) and inputs[3]!=1:
                ge[x].fitness -= 5
            if(output[1] == max(output)) and inputs[4]!=1:
                ge[x].fitness -= 5
            if(output[2] == max(output)) and inputs[5]!=1:
                ge[x].fitness -= 5

            if output[1] == max(output): # take left
                if snake.direction == 'n':
                    snake.direction = 'w'
                elif snake.direction == 'w':
                    snake.direction = 's'
                elif snake.direction == 's':
                    snake.direction = 'e'
                elif snake.direction == 'e':
                    snake.direction = 'n'
                        
            elif output[2] == max(output): # take right
                if snake.direction == 'n':
                    snake.direction = 'e'
                elif snake.direction == 'e':
                    snake.direction = 's'
                elif snake.direction == 's':
                    snake.direction = 'w'
                elif snake.direction == 'w':
                    snake.direction = 'n'
    
                
        for i, snake in enumerate(snakes):
            dead = False
            if snake.die(window_x, window_y):
                dead = True
                ge[i].fitness -= 8
                fruits.pop(i)
                snakes.pop(i)
                nets.pop(i)
                ge.pop(i)
                if len(snakes) == 0:
                    Run = False
                    break
                
            if ( not dead ) and snake.steps > snake.life:
                dead = True
                ge[i].fitness -= 10
                fruits.pop(i)
                snakes.pop(i)
                nets.pop(i)
                ge.pop(i)
                if len(snakes) == 0:
                    Run = False
                    break
                
            if (not dead) and snake.x == fruits[i].x and snake.y == fruits[i].y:
        
                fruits[i].x = random.randrange(1, (window_x//10)) * 10
                fruits[i].y = random.randrange(1, (window_y//10)) * 10
                snake.score += 1
                snake.grow()
                if(snake.score > max_score):
                    max_score = snake.score
                ge[i].fitness += 50
                snake.life += 100
                
        screen.fill(black)
        
        for fruit in fruits:
            fruit.draw(screen)
        
        for snake in snakes:
            snake.draw(screen)
            
        show_score(1, white, 'times new roman', 20, max_score)
        
        pygame.display.update()
        fps.tick(snake_speed)
        
    generation_count += 1

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)    
    
    # store the stats per generation in a file
    p.add_reporter(neat.Checkpointer(5, filename_prefix='checkpoints/neat-checkpoint-'))
    
    winner = p.run(eval_genomes, 50)
    
    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))
    
def runCheckpoint(config_path, checkpoint):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Checkpointer.restore_checkpoint(checkpoint)
    global generation_count
    generation_count = p.generation
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    
    # store the stats per generation in a file
    p.add_reporter(neat.Checkpointer(5, filename_prefix='checkpoints/neat-checkpoint-'))
    
    winner = p.run(eval_genomes, 50)
    
    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))
    
    return stats.generation_statistics[0]['generation'], stats.generation_statistics[0]['max']
 
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)


