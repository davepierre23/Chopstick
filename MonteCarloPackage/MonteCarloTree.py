from Model.Game import ChopStickGame
from MonteCarloPackage.MonteCarloNode import MonteCarloNode
from Model.Common import *

node_count = 0
class MonteCarloTreeSearch:

    def __init__(self):
        self.name = "Monte Carlo Tree Search"


    def __eq__(self, other):
        return self.equals(other)

    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def toString(self):
        return self.name

    def equals(self, other):
        return self.name == other.name

    def searchMove(self,gameState,  maximizingPlayerId,depthLimit=2):


        move =self.monte_carlo_tree_search(gameState,maximizingPlayerId, depthLimit)


        return move



    def monte_carlo_tree_search(self,initalState,playerNum, depthSearch):

        print("Monte Carlo Tree Search")

        # create the Root node
        root = MonteCarloNode(initalState,None,None,0, playerNum)
        root.setCurrentPlayerId(playerNum)
        root.explored()

        # create the childList

        leaf = self.select(root)
        simulation_result = self.simulate(leaf, playerNum)
        self.backpropagate(leaf, simulation_result)
        while(depthSearch+1 > leaf.getDepth()):
            leaf = self.select(root)
            simulation_result = self.simulate(leaf, playerNum)
            self.backpropagate(leaf, simulation_result)

        bestNode = self.best_child(root)

        bestAction = bestNode.action
        return bestAction






    # This will traverse the tree until it has found a leaf node
    def select(self,node):

        #if a node is a leafNode
        if(node.isUnexplored()):
            node.explored()
            return node


        for child in node.getChildren():
            if(child.isUnexplored()):
                child.explored()
                return child

        bestVal = -math.inf;
        result = node
        for child in node.getChildren():
            val = max(bestVal,self.uctVal(child))
            if(val != bestVal):
                bestVal = val
                result= child


        return self.select(result)




    def getScore(self,winnerPlayerId,maxmizingPlayerID):
        if(winnerPlayerId == maxmizingPlayerID):
            return 1
        else:
            return 0

    def backpropagate(self,node,score):
        node.visitNode()
        # score is either
        node.numOfWins = node.numOfWins +score

        if node.parent:
            self.backpropagate(node.parent, score)

    def uctVal(self,node):

        # one argulemt is the base of natural log
        naturalLogParentVist = math.log(node.getParent().getNumVisit())
        secondPart = math.sqrt(naturalLogParentVist/ node.getNumVisit())
        winrate = node.getWinRate()

        return winrate + secondPart



    def simulate(self,node, currentPlayerID):

        # every time we simulate we create a node
        global node_count
        node_count = node_count +1

        # create a game so that we can simulate
        game = ChopStickGame(True)

        # create random Players with the intial State
        randomGame = game.makeRandomGame(node.getState(), currentPlayerID)

        playerIDWinner = randomGame.rungame()

        winnerOrLoser = self.getScore(playerIDWinner, currentPlayerID)
        return  winnerOrLoser

    def backpropagate(self,node,score):
        #
        node.setNumVisit(node.getNumVisit()+1)
        if(node.parent):
            self.backpropagate(node.parent,score)

    def best_child(self,root):
        bestScore =  -math.inf
        bestNode = None
        for child in root.getChildren():
            if(child.getWinRate()> bestScore):
                bestNode = child

        return bestNode

if __name__ == '__main__':


    algo = MonteCarloTreeSearch()










