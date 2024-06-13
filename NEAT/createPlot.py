# we will use population_fitness.txt to create a plot

import matplotlib.pyplot as plt

def createPlots():
    with open('./population_fitness.txt', 'r') as f:
        data = f.read()
        
    data = data.split('\n')
    x = []
    y1 = []
    y2 = []
    
    for i in range(len(data)):
        if len(data[i]) > 1:
            a, b = data[i].split(' ')
            x.append(i)
            y1.append(float(a))
            y2.append(float(b))
            
    plt.plot(x, y1, label='Average Fitness')
    plt.plot(x, y2, label='Best Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.legend()
    plt.show()
            
createPlots()