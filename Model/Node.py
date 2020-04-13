z
class Node():
    def __init__(self,state,parent,action,pathCost,depth):
        self.state = state #used has the state of the game
        self.parent = parent # used to keep track of the parent
        self.action = action # the action of the gameState
        self.g = pathCost  #the cost from the c
        self.h = state.heuristic() # gameState using heuristic
        self.depth = depth  # the depth of it
        self.f = self.depth+ self.h # the total cost from the cost from the heurisitic and total cost to get here

    def __str__(self):
        return str(self.action)

    def __eq__(self, other):
        return self.state == other.state

