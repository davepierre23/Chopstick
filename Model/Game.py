
from GameBoard import * 

class ChopStickGame:
    def __init__(self):

        numOfPlayers = self.getGameInput()
        self.board = GameBoard(numOfPlayers)
        self.currentPlayer =1  # returns random player

    def changePlayer(self):
        self.currentPlayer = self.board.changePlayer(self.currentPlayer)

    def getCurrentPlayerId(self):
        return self.currentPlayer

    def getCurrentPlayer(self):
        currentPlayer = self.players[self.currentPlayer-1]
        return currentPlayer

    def getGameInput(self):
        print("How many Players would you like for Chopsticks")

        numPlayers = -1
        
        while(numPlayers<0):
            numPlayers = int(input("Enter your choice now for the number Of Players"))

        return numPlayers
    def rungame(self):

        numOfRounds =0
        while (not(self.board.isGameOver())):
            numOfRounds += 1
            print("Currently Player " + str(self.getCurrentPlayerId())+" turn  ")
            playerId = self.getCurrentPlayerId()
            self.board.make_move(playerId)

        print(self.board)
        self.board.getWinner()



def main():
    game = ChopStickGame()
    game.rungame()




if __name__ == '__main__':
    main()
