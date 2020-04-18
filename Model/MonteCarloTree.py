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
    if(node.getVisit()==0):
        return node

    for child in node.getChildern():
        if(child.getVisit()==0):
            return child

    bestVal = 0;
    result = node
    for child in node.getChildern():
        val = max(bestVal,uctVal(child))
        if(val != bestVal):
            bestVal = val
            result= child


    return result


def expand(node):
    actions = getActions()
    for action in actions:

def backpropagate(node,score):
    node.visits= node.visits +1
    node.utility = node.utlity+ score

    if node.parent:
        backpropagate(node.parent, score)

def uctVal(node):

    # one argulemt is the base of natural log
    naturalLogParentVist = math.log(node.getParent().getVisit())
    secondPart = math.sqrt(naturalLogParentVist/ node.getVisit())
    winrate = node.getWinRate()

    return winrate + secondPart
def UCT(gameState,depth):


    #Create root node



