class Node():
    def __init__(self,state,parent,action,depth):
        self.state = state #used has the state of the game
        self.parent = parent # used to keep track of the parent
        self.action = action # the action of the gameState
        self.depth = depth  # the depth of it
  
    def __str__(self):
        string = str(self.state)
        string += "\n"
        string += "depth : " + str(self.depth)
        return string

    def __eq__(self, other):
        return self.state == other.state

