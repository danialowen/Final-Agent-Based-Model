# Import the necessary packages and files 
import random
import matplotlib.pyplot
import matplotlib.animation
import agentframework  # The module which gives agents their random location, make them eat, move, etc. 
import csv

# Set the conditions; number of agents, iterations and neighbourhood distance
num_of_agents = 10          
num_of_iterations = 5         
agents = []                      
neighbourhood = 20          


# Create an environment to append the values 
f = open('in.txt', newline='')
environment = []
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()


# Create the "fig" ready for later stages and set axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    

# Create the for loops under update class that will be used in the animation. 
# The for loops place the agents in the environment and makes them move, share
# food with neighbouring agents and eat until they are full (self.store >= 5000)

def update(frame_number):
    
    fig.clear()   
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_iterations):  # 5 iterations each loop
        random.shuffle(agents)
        for i in range (num_of_agents):  # All function below in agentframework.py
            agents[i].move()
            agents[i].eat_until_full()  # Function stops once all agents have self.store value >= 5000
            agents[i].share_with_neighbours(neighbourhood)


# Plot the agents and their functions, the colour, shape and size have been amended               
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, edgecolor="white",
                                  color="white", marker="X", s=100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlim(0, 100)
    
# Create the animation, displaying the fig whilst calling the for loops and functions

animation = matplotlib.animation.FuncAnimation(fig, update)

#Show fig

matplotlib.pyplot.show()    


# %matplotlib qt - type into console to open animation window