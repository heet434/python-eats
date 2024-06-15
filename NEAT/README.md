# NEAT (NeuroEvolution of Augmenting Topologies)

This folder contains the implementation of NEAT algorithm through multiple generations to obtain a neural network that can guide the snake to score more than 50 in less than 15 generations. <br/>
We use [neat-python](https://github.com/CodeReclaimers/neat-python) for evolution of the neural network and [pygame](https://github.com/pygame/pygame) for the UI of the snakes.<br/>
Here is a demo of the best and the last surviving snake from generation 16, that easily scored beyond 50.</br>

https://github.com/heet434/python-eats/assets/118350153/b01bf0d9-d8d5-4a1d-bd8d-6265104a0d09

---
### Neural Network: Input and Outputs
The neural network is initialized with 9 input neurons and 3 output neurons. There are 0 hidden neurons initially.<br/>
The 9 input values we feed to the network are if food is in front, left or right, if snake can move forward, left or right without it touching a wall and if snake can move forward, left or right without it touching its own body.<br/>
The 3 output values signify if the snake should move forward, left or right.<br/>

---
### Configuration of NEAT algorithm
The population size is set to 100. As the performance of NEAT algorithm depends highly on the population size, at a size of 100, the snakes learned to avoid walls in 2 generations, eat food in 2-3 generations and avoid its body in 14-15 generations. At a size of 1000, in 2 generations they learned all of this.<br/>
We have set the elitism, both species and for reproduction to 3, and the survival threshold to 0.3. ReLU Activation function is used for the neurons. Other specifications can be seen in the config-feedforward.txt file.<br/>
The fitness function we use gives +50 for eating food, -8 for dying due to wall or itself, -10 for running out of life (initial life is set to 200 and decrements on each step, and is increased by 100 on eating food), -5 if the output by neural network causes snake to die.

<br/>
When you run "game.py", this is how it will look initially as you are viewing all the snakes from this generation at once. Then gradually snakes will die due to various reasons one by one and the fittest snakes of the generation will clearly emerge out. 
<img width="301" alt="Screenshot 2024-06-13 at 11 51 28 PM" src="https://github.com/heet434/python-eats/assets/118350153/c098fa12-5fd7-4da7-9ca3-31f0711a966a">


---
### Setup
1. Clone the repository. <br/>
2. Install the requirements using ``pip install -r requirements.txt``
3. Start the generational training as mentioned in the next section by using ``python game.py``


--- 
### Starting the generations
To start from generation 0 and view the evolution process of all the snakes, just run the "game.py" program. We have set the default board size as 300x300 pixels, i.e. 30x30 blocks. </br>
We ran the evolution process till 20 generations and stored the genomes at some checkpoints (i.e. some generations). They are stored as binary pickle files in the checkpoints folder. To load up a particular generation and start the process from there, use the "runCheckpoint.py" program and set your saved generation number in "runCheckpointNo" variable. Also note that every time you run the process of evolution, the checkpoints at particular generations will be rewritten. <br/>
Here is a graph of fitness vs generations:<br/>
<img align = "center" width="637" alt="population_fitness" src="https://github.com/heet434/python-eats/assets/118350153/7677f9e8-48cf-48f6-ace1-b67427f68dd1">



