
from GameBoard import *
from AiPlayer import AiPlayer
from Paranoid import Paranoid
from Max_n import Max_n
from BestReply import  BestReply
from RandomPlay import RandomPlay
from copy import deepcopy

import time
class ChopStickGame:
    numOfAlgo = 3
    def __init__(self):

        self.numOfPlayers = 3
        self.board = GameBoard(self.numOfPlayers)
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
            if(playerId % self.numOfAlgo==0):
                players[playerId] = AiPlayer(playerId,Paranoid())

            elif(playerId %self.numOfAlgo==1):
                players[playerId] = AiPlayer(playerId, Max_n())

            elif(playerId %self.numOfAlgo==2):
                players[playerId] = AiPlayer(playerId, BestReply())

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



def main():
    game = ChopStickGame()
    game.rungame()




if __name__ == '__main__':
    loop= []
    for i in range(10):
        game = ChopStickGame()
        randomGame = game.makeRandomGame(game.getBoard(), 1)
        loop.append(randomGame.rungame())

    print(loop)

