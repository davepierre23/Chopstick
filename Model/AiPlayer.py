
class AiPlayer:

    def __init__(self, playerId, algorithem,heuristicNumber):
        self.playerId = playerId
        self.heuristicNumber = heuristicNumber
        self.algo
        self.move = []

    def getId(self):
        return self.playerId

    def getMove(self, board):
        move = self.algo.runAlgo()
        return move


    def getScore(self,board):
        score = 0
        if(self.heuristicNumber==1):
            score+= board.heuristic1(self.playerId)
        elif(self.heuristicNumber==2):
            score +=board.heuristic2(self.playerId)

        return score


    def __str__(self):
        return self.toString()
    def __repr__(self):
        return self.toString()

    def toString(self):
        string= "Ai player" + " Player Id " + str(self.playerId)+ " "+str(self.move)

        return string
