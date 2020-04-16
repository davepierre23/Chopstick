from copy import deepcopy
from Node import Node

def get_path(node):
    node
    path = []
    path.insert(0, node.action)
    parent = node.parent
    while parent:
        path.insert(0, parent.action)
        parent = parent.parent

    return path

def getParent(node):
    node
    path = []
    path.insert(0, node)
    parent = node.parent
    while parent:
        path.insert(0, parent)
        parent = parent.parent

    return path
def heuristic(node,playerId):
    # this will evaluate how manyy players are currnt alive ohter then itself
    numberOfPlayers = 0
    gameBoard = node.state.board
    for playerBoard  in gameBoard:
        if(gameBoard[playerBoard].isPlayerAlive() and playerId != gameBoard[playerBoard].getId()):
             numberOfPlayers +=1

    return numberOfPlayers


def generateChildState(initNode, currentPlayerId):
    possibleMoves = initNode.state.generateAllPossibleMoves(currentPlayerId)

    childNodeList = []
    for move in possibleMoves:
        childState = deepcopy(initNode.state)
        childState.make_move(currentPlayerId, move)
        childNode = Node(childState, initNode, move, initNode.depth + 1)
        childNodeList.append(childNode)

    return childNodeList