# Python-Eats: Snake AI
This project explores the application of two advanced machine learning algorithms—NEAT (NeuroEvolution of Augmenting Topologies) and Deep Q-Learning—to create intelligent agents capable of playing the classic Snake game. We use Pygame for the game's user interface, NEAT-Python for the NEAT algorithm, and PyTorch for the Deep Q-Learning algorithm.

## Algorithms Overview
### NEAT
NEAT (NeuroEvolution of Augmenting Topologies) is a genetic algorithm that evolves neural networks over successive generations. It starts with a simple network and gradually increases its complexity by adding new nodes and connections through mutations. The NEAT algorithm is well-suited for problems where the solution structure is not known in advance.

#### Key Characteristics:

Initial Population: 100 <br/>
Generations to Achieve Score of 75: 15 <br/>
Library Used: neat-python

### Deep Q-Learning
Deep Q-Learning is a reinforcement learning algorithm that combines Q-Learning with deep neural networks. The agent learns to play the game by interacting with the environment, receiving rewards for certain actions, and updating its knowledge to maximize cumulative rewards.

#### Key Characteristics:

Iterations to Achieve Score of 75: 100 <br/>
Library Used: PyTorch

----

## Performance Comparison
The performance of the two algorithms is evaluated based on their ability to achieve a score of 75 in the Snake game.

### NEAT: 
Achieved a score of 75 in approximately 15 generations with an initial population of 100.
### Deep Q-Learning: 
Achieved a score of 75 after about 100 iterations.

----
While Deep Q-Learning required more iterations to reach the target score, NEAT achieved the same score in fewer generations but with a larger population size.
