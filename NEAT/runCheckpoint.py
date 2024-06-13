import os
import neat
import time
import random

import game

runCheckpointNo = 14

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    checkpoint = os.path.join(local_dir, './checkpoints/neat-checkpoint-{}'.format(runCheckpointNo))
    
    game.runCheckpoint(config_path, checkpoint)
    