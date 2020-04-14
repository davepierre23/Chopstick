
from GameBoard import * 

class ChopStickGame:
    def __init__(self):

        numOfPlayers = self.getGameInput()
        self.board = GameBoard(numOfPlayers)
        self.players = self.createPlayers(numOfPlayers)
        self.currentPlayer =1  # returns random player

    def switchPlayer(self):
        if (self.currentPlayer ==1):
            self.currentPlayer =2
        else :
            self.currentPlayer =1

        print(self.getCurrentPlayer())

    def getCurrentPlayerId(self):
        return self.currentPlayer
    def getCurrentPlayer(self):
        currentPlayer = self.players[self.currentPlayer-1]
        return currentPlayer

    def createPlayers(self, gameMode):
        players = []
        if (gameMode == 1):
            players.append(self.createHumanPlayer(1))
            choiceheuristic = int(input("Enter 1 for heuristic one and 2 for heuristic"))

            while choiceheuristic != 1 and choiceheuristic != 2:
                choiceheuristic = int(input("Enter 1 for heuristic one and 2 for heuristic"))

            players.append(self.createAiPlayer(2,choiceheuristic))

        elif(gameMode ==2):
            players.append(self.createAiPlayer(1, 1))
            players.append(self.createAiPlayer(2, 2))


        elif (gameMode == 3):
            players.append(self.createHumanPlayer(1))
            players.append(self.createHumanPlayer(2))


        return players




    def createHumanPlayer(self,playerId):
        hplayer = HumanPlayer(playerId)
        return hplayer
    def createAiPlayer(self,playerId, heuristicNumber):
        aiPlayer = AiPlayer(playerId,heuristicNumber)
        return aiPlayer


    def getGameInput(self):
        print("How many Players would you like for Chopsticks")
       

        numPlayers = -1
        
        while(numPlayers<0):
            numPlayers = int(input("Enter your choice now for the number Of Players"))


    def rungame(self):
        print("Intial State")
        printBoard(self.board)
        input("ENTER TO CON")

        while (not(self.board.isGameOver())):
            print("Currently Player " + str(self.getCurrentPlayerId())+" turn  ")
            player = self.getCurrentPlayer()
            self.board.make_move(player)
            self.switchPlayer()

        self.board.getWinner()
        printBoard(self.board)

def main():
    mancalaGame = Game()
    mancalaGame.rungame()




if __name__ == '__main__':
    main()
