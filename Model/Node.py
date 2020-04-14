z
class Node():
    def __init__(self,state,parent,action,depth):
        self.state = state #used has the state of the game
        self.parent = parent # used to keep track of the parent
        self.action = action # the action of the gameState
        self.score = state.heuristic() # gameState using heuristic
        self.depth = depth  # the depth of it
  
    def __str__(self):
        return str(self.action)

    def __eq__(self, other):
        return self.state == other.state

