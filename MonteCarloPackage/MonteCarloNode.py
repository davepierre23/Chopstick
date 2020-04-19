class Node():
    def __init__(self, state, parent, action, depth):
        self.state = state  # used has the state of the game
        self.parent = parent  # used to keep track of the parent
        self.action = action  # the action of the gameState
        self.depth = depth  # the depth of it
        self.numVisit = 0
        self.children= self.generateChildren()
        self.utility = 0

    def __str__(self):
        string = str(self.state)
        string += "\n"
        string += "depth : " + str(self.depth)
        return string

    def __repr__(self):
        return self.toString()

    def getParent(self):
        return self.parent
    def getUtility(self):
        return self.utility

    def setUtility(self, val):
        self.utility

    def getNumVisit(self):
        return self.numVisit
    def setNumVisit(self, numvisits):
        self.numVisit = numvisits

    def generateChildren(self):
        pass

    def getChildren(self):
        return self.children

    def cutOff_test(self, depth):
        return self.state.isGameOver() or depth == 0

    def toString(self):
        string = str(self.state)
        string += "\n"
        string += "depth : " + str(self.depth)
        return string

    def __eq__(self, other):
        return self.state == other.state

    def isUnexplored(self):
        return self.numVisit ==0

import math
# main function for the Monte Carlo Tree Search
def monte_carlo_tree_search(root):
    while resources_left(time, computational power):
        leaf = traverse(root)
        simulation_result = rollout(leaf)
        backpropagate(leaf, simulation_result)

    return best_child(root)


# function for node traversal
def traverse(node):
    while fully_expanded(node):
        node = best_uct(node)

        # in case no children are present / node is terminal
    return pick_univisted(node.children) or node


# function for the result of the simulation
def rollout(node):
    while non_terminal(node):
        node = rollout_policy(node)
    return result(node)


# function for randomly selecting a child node
def rollout_policy(node):
    return pick_random(node.children)


# function for backpropagation
def backpropagate(node, result):
    if is_root(node) return
    node.stats = update_stats(node, result)
    backpropagate(node.parent)


# function for selecting the best child
# node with highest number of visits
def best_child(node):
    pick
    child
    with highest number of visits




def select(node):
    if(node.isUnexplored()):
        return node

    for child in node.getChildren():
        if(child.isUnexplored()):
            return child

    bestVal = 0;
    result = node
    for child in node.getChildren():
        val = max(bestVal,uctVal(child))
        if(val != bestVal):
            bestVal = val
            result= child


    return select(result)


def expand(node):
    actions = getActions()
    for action in actions:

def backpropagate(node,score):
    node.setNumVisit(node.getNumVisit() +1)
    node.utility = node.utlity+ score

    if node.parent:
        backpropagate(node.parent, score)

def uctVal(node):

    # one arguement is the base of natural log


    naturalLogParentVist = math.log(node.getParent().getNumVisit())
    secondPart = math.sqrt(naturalLogParentVist/ node.getNumVisit())
    winrate = node.getWinRate()

    return winrate + secondPart



def expand(node):
    actions = node.getState().generateMoveSet()

    for action in actions:
        pass

def simulate(state):
    pass

def backpropagate(node,score):
    node.setNumVisit(node.getNumVisit+1)
    node.setUtility(node.getUtility()+ score)

    if(node.parent):
        backpropagate(node.parent,score)



def UCT(gameState,depth):
    pass


    #Create root node



