from copy import deepcopy
class MonteCarloNode:
    def __init__(self, state, parent, action, depth, currentplayerId):
        self.state = state  # used has the state of the game
        self.parent = parent  # used to keep track of the parent
        self.action = action  # the action of the gameState
        self.depth = depth  # the depth of it
        self.children = None
        self.currentPlayerId = currentplayerId
        self.numVisit = 0
        self.numOfWins = 0
        self.numOfStimulations = 0
        self.hasExplored = False

    def __str__(self):
        string = str(self.state)
        string += "\n"
        string += "depth : " + str(self.depth)
        return string

    def __repr__(self):
        return self.toString()

    def getState(self):
        return self.state
    def getDepth(self):
        return self.depth
    def setCurrentPlayerId(self, currentPlayerId):
        self.currentPlayerId = currentPlayerId

    def getCurrentPlayerId(self):
        return self.currentPlayerId
    def getParent(self):
        return self.parent

    def getNumOfWins(self):
        return self.numOfWins

    def increaseWin(self):
        self.numOfWins = self.numOfWins +1
    def setNumOfWin(self, win):
        self.numOfWins = win
    def getNumberOfSimulation(self):
        return self.numOfStimulations

    def increaseStmulation(self):
        self.numOfStimulations = self.numOfStimulations  +1

    def setNumStumlation(self,numOfStmulation):
        self.numOfStimulations= numOfStmulation

    def getWinRate(self):
        return self.numOfWins / self.numVisit

    def getNumVisit(self):
        return self.numVisit
    def visitNode(self):
        self.numVisit = self.numVisit +1

    def setNumVisit(self, numvisits):
        self.numVisit = numvisits

    def generateChildren(self):
        node = self

        if(self.state.cutOff_test(1000)):
            return []
        currentPlayerId = node.getCurrentPlayerId()
        possibleMoves = node.state.generateAllPossibleMoves(currentPlayerId)
        childNodeList = []
        for move in possibleMoves:
            childState = deepcopy(node.state)
            childState.make_move(currentPlayerId, move)
            nextPlayerID = childState.changePlayer(currentPlayerId)
            childNode = MonteCarloNode(childState, node, move, node.depth + 1, nextPlayerID)
            childNode.setCurrentPlayerId(nextPlayerID)
            childNodeList.append(childNode)

        return childNodeList

    def getChildren(self):
        if(not(self.children)):
            self.children = self.generateChildren()

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
        return not(self.hasExplored)

    def explored(self):
        self.hasExplored = True




