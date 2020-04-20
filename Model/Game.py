
from GameBoard import *
from AiPlayer import AiPlayer
from Paranoid import Paranoid
from Max_n import Max_n
from BestReply import  BestReply
from RandomPlay import RandomPlay

from copy import deepcopy
from Model.MCT import *


class ChopStickGame:
    numOfAlgo = 3
    def __init__(self,createRandomPlayer=False):

        self.numOfPlayers = 4
        self.board = GameBoard(self.numOfPlayers)
        if(createRandomPlayer):
            self.players = self.replacePlayersWithRandomPlayer()

        else:
            self.players = self.createPlayers(self.board)
        self.currentPlayerId =1  # returns random player



    def changePlayer(self):
        self.currentPlayerId = self.board.changePlayer(self.currentPlayerId)

    def makeRandomGame(self,setGame,nextPlayerId):

        newGame = ChopStickGame()
        currentGameState = deepcopy(setGame)
        newGame.setBoard(currentGameState)
        newGame.setCurrentPlayerId(nextPlayerId)
        newGame.replacePlayersWithRandomPlayer()


        return newGame

    def replacePlayersWithRandomPlayer(self):
        players = {}
        for playerId in self.board.board:
            players[playerId] = AiPlayer(playerId, RandomPlay())


        self.players = players
        return players


    def getNumRound(self):
        return self.numRounds

    def setNumRound(self, numOfRounds):
        self.numRounds = numOfRounds

    def getBoard(self):
        return self.board
    def setBoard(self, stateBoard):
        self.board = stateBoard

    def setCurrentPlayerId(self,playerId):
        self.currentPlayerId = playerId


    def getCurrentPlayerId(self):
        return self.currentPlayerId

    def getCurrentPlayer(self):
        currentPlayer = self.players[self.currentPlayerId]
        return currentPlayer

    def getCurrentPlayerMove(self):
        currentPlayer=self.getCurrentPlayer()
        move = currentPlayer.getMove(self.board)
        return move

    def getGameInput(self):
        print("How many Players would you like for Chopsticks")

        numPlayers = -1
        
        while(numPlayers<0):
            numPlayers = int(input("Enter your choice now for the number Of Players"))


        self.numOfPlayers = numPlayers
        return numPlayers

    def getNumOfPlayers(self):
        return self.numOfPlayers

    def setNumOfPlayers(self, numOfPlayers):
        self.numOfPlayers = numOfPlayers

    def createPlayers(self,gameBoard):

        players = {}
        for playerId in gameBoard.board:
            if(playerId % self.numOfAlgo==3):
                players[playerId] = AiPlayer(playerId,Paranoid())

            elif(playerId %self.numOfAlgo==1):
                players[playerId] = AiPlayer(playerId, Max_n())

            elif(playerId %self.numOfAlgo==2):
                players[playerId] = AiPlayer(playerId, BestReply())

            elif(playerId%self.numOfAlgo ==0):
                algo = MCTSearch()
                players[playerId] = AiPlayer(playerId,Paranoid())

        return players

    def rungame(self):

        numOfRounds =0
        while (not(self.board.isGameOver())):
            numOfRounds += 1
            print("Currently Player " + str(self.getCurrentPlayerId())+" turn  ")
            playerId = self.getCurrentPlayerId()
            move = self.getCurrentPlayerMove()
            self.board.make_move(playerId,move)
            print(self.board)

            self.changePlayer()

        print(self.board)
        return self.board.getWinner()

from Game import *
from MCTNode import MonteCarloNode
from Common import *
import math

from Model.Game import ChopStickGame

node_count = 0
class MCTSearch:

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



    def monte_carlo_tree_search(self,initalState,playerNum, depthSearch=2, second=30):

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









def main():
    game = ChopStickGame()
    game.rungame()




if __name__ == '__main__':
    main()
    # import datetime
    # start = datetime.datetime.now()
    # while True:
    #     print("Math test. Add , dont screw up, you got {}s left".
    #           format(20 - (datetime.datetime.now() - start).seconds))
    #
    #
    #     if (datetime.datetime.now() - start).seconds > 30:
    #         print("Times up")
    #         break




