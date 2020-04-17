
class AiPlayer:

    def __init__(self, playerId, algorithem):
        self.playerId = playerId
        self.algo = algorithem
        self.move = []

    def getId(self):
        return self.playerId

    def getMove(self, board):
        move = self.algo.searchMove(board,self.playerId)
        return move


    def __str__(self):
        return self.toString()
    def __repr__(self):
        return self.toString()

    def toString(self):
        string= "Ai player" + " Player Id " + str(self.playerId)+ " "+str(self.move)

        return string
