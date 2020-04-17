
from GameBoard import *
from AiPlayer import AiPlayer
from Paranoid import Paranoid
from Max_n import Max_n
from BestReply import  BestReply

class ChopStickGame:
    numOfAlgo = 3
    def __init__(self):

        numOfPlayers = 3

        self.board = GameBoard(numOfPlayers)
        self.players = self.createPlayers(self.board)
        self.currentPlayer =1  # returns random player


    def changePlayer(self):
        self.currentPlayer = self.board.changePlayer(self.currentPlayer)

    def getCurrentPlayerId(self):
        return self.currentPlayer

    def getCurrentPlayer(self):
        currentPlayer = self.players[self.currentPlayer]
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


        return numPlayers

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

            self.changePlayer()

        print(self.board)
        self.board.getWinner()



def main():
    game = ChopStickGame()
    game.rungame()




if __name__ == '__main__':
    main()
