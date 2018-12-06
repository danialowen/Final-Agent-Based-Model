import random

class Agent:
    def __init__(self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents
        
    def move(self):
        #if the random number is below 0.5, the x and y coordinates must move 
        #postition by +1 from its original value. If more than 0.5, move -1
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
    
    def eat_until_full(self): 
        # Eating the environment as they move and gaining +10 in thier store 
        # until all agents are full (defined by a store of >= 5000) and then stop
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        if self.store >= 5000:
            self.move = 0
            
                      
    def share_with_neighbours(self, neighbourhood):
        # If the agents come close enough to eachother, shorter than the value of 
        # neighbourhood, then they share the food and share store value
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave  
    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
