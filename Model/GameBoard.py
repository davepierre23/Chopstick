from PlayerHands import PlayerHandsfrom Node import Nodefrom copy import deepcopyfrom Paranoid import Paranoidfrom Max_n import Max_nfrom BestReply import  BestReplyimport logginglogging.basicConfig(level=logging.INFO)import mathnode_count = 0# FFor now is used has the stateclass GameBoard:    HIT = 0    SPLIT = 1    def __init__(self,numPlayer =4,currentIndex=1):        self.IsGameOver = False  # to see if tis gameover        self.board = self.createGameBoard(numPlayer)        self.numPlayer = numPlayer        self.currentPlayer = currentIndex       def __eq__(self, other):        return self.equals(other)    def __str__(self):        return self.toString()    def __repr__(self):        return self.toString()    def createGameBoard(self, numberOfPlayers):        #Game board that has all the player chopstick        gameBoard= {}        for playerId in range(1,numberOfPlayers+1):            gameBoard[playerId] = PlayerHands(playerId)        return gameBoard        def toString(self):        stringVersion = ""        for boardId in self.board:            stringVersion += str(self.board[boardId])            stringVersion +="\n"        return stringVersion      def getPlayerHandAt(self, index):        return self.board[index]    def equals(self, other):        # if every piece in the mancala are equal        return self.board == other.board    def isGameOver(self):        numberOfAlive = 0        for playerBoard in self.board:            if(self.board[playerBoard].isPlayerAlive()):                numberOfAlive += 1                return numberOfAlive == 1             def getWinner(self):        if(self.isGameOver()):                    for playerBoard in self.board:                if(self.board[playerBoard].isPlayerAlive()):                    print("The winner pf the game is player Id", self.board[playerBoard].getId())                    return playerBoard                    print("There was not any winner")    def generateAllPossibleMoves(self,playerId):        moveList = []        hitMoves = self.generateHitPossibleMoves(playerId)        for move in hitMoves:            moveList.append(move)                   #for now can split at anytime but cant be the same pair         splitMoves = self.generateSplitPossibleMoves(playerId)        for move in splitMoves:             moveList.append(move)                return moveList    def generateSplitPossibleMoves(self,playerId):        #get playerBoard        playerBoard = self.getPlayerHandAt(playerId)        #        totalNumSticks = 0         leftHandNum = playerBoard.getNumOfStickLeftHand()        rightHandNum = playerBoard.getNumOfStickRightHand()        totalNumSticks += leftHandNum        totalNumSticks += rightHandNum        # generate all the possible ways to split         moveList = []        # to check if dont want duplicates        handSeen = set()        handSeen.add(leftHandNum)        handSeen.add(rightHandNum)        if (totalNumSticks == 1):            return moveList        for i in range(0,totalNumSticks):            rightHand = totalNumSticks - i            leftHand = i             if(not(leftHand in handSeen and rightHand in handSeen)):                if(rightHand < playerBoard.LIMIT and leftHand < playerBoard.LIMIT):                    aMove=[]                    aMove.append(self.SPLIT)                    aMove.append(leftHand)                    aMove.append(rightHand)                    moveList.append(aMove)                    #TODO: get rid of duplicates        return moveList    def generateHitPossibleMoves(self,playerId):        moveList = []        playerTurn = self.getPlayerHandAt(playerId)        #A move will be a list        # HIT or SPLIT : 0 index        # choice hand of had to hit with : 1 index        # playerID to hit with 2 index        # LEFT ot RIGHT to hit the other player hand : 3 index        for aPlayerId in self.board:            playerBoard = self.board[aPlayerId]            # if the player does not have the same player ID has the playerBoard            if(playerId != playerBoard.getId()):                if(playerTurn.isLeftHandAlive()):                    leftToAttackChoice = playerTurn.LEFT                    leftHitMove = []                    leftHitMove.append(self.HIT)                    leftHitMove.append(leftToAttackChoice)                    playerIdToHit = playerBoard.getId()                    leftHitMove.append(playerIdToHit)                    # left hand hits the left hand of the other if both are alive                    if(playerBoard.isLeftHandAlive()):                                                aMove = deepcopy(leftHitMove)                        aMove.append(playerBoard.LEFT)                         moveList.append(aMove)                    # left hand hits the right of the other if both are alive                     if(playerBoard.isRightHandAlive()):                        aMove = deepcopy(leftHitMove)                        aMove.append(playerBoard.RIGHT)                        moveList.append(aMove)                                                        if(playerTurn.isRightHandAlive()):                    rightToAttackChoice = playerTurn.RIGHT                    rightHitmove = []                    rightHitmove.append(self.HIT)                    rightHitmove.append(rightToAttackChoice)                    playerIdToHit = playerBoard.getId()                    rightHitmove.append(playerIdToHit)                    # right hand hits the left hand of the other if both are alive                    if(playerBoard.isLeftHandAlive()):                        aMove = deepcopy(rightHitmove)                        aMove.append(playerBoard.LEFT)                        moveList.append(aMove)                    # right hand hits the right hand of the other player                    if(playerBoard.isRightHandAlive()):                        aMove = deepcopy(rightHitmove)                        aMove.append(playerBoard.RIGHT)                        moveList.append(aMove)        return moveList    def applySplitChoice(self,playerId,move):        playerBoard = self.getPlayerHandAt(playerId)        leftHand = move[1]        rightHand = move[2]        playerBoard.setNumOfStickLeftHand(leftHand)        playerBoard.setNumOfStickRightHand(rightHand)    def applyHitChoice(self,playerId,move):        playerBoard = self.getPlayerHandAt(playerId)        currentPlayerHandChoice = move[1]        playerHandChoiceNumber = playerBoard.getHandOfChoice(currentPlayerHandChoice)        playerHandToHit = self.getPlayerHandAt(move[2])        oppHand = move[1]        playerHandToHit.hit(oppHand,playerHandChoiceNumber)    def isSplitMove(self, move):        return move[0] == self.SPLIT        def isHitMove(self, move):        return move[0] == self.HIT    def make_move(self, currentPlayerId, move):        if (self.isGameOver()):            return        # if the move was SPLIT move         if (self.isSplitMove(move)):            self.applySplitChoice(currentPlayerId,move)                            else:           # if it was a hit move            self.applyHitChoice(currentPlayerId, move)                  def cutOff_test(self, depth):        return self.isGameOver() or depth == 0    def changePlayer(self, playerId):                nextPlayerId = playerId +1        while nextPlayerId != playerId :            if nextPlayerId >self.numPlayer :                nextPlayerId =1            nextPlayerBoard = self.getPlayerHandAt(nextPlayerId)            #the next player should have at least one Hand alive            if(nextPlayerBoard.isPlayerAlive()):                return nextPlayerBoard.getId()            else:                nextPlayerId = nextPlayerId + 1        print("I have only one person left ")        return playerId    def getAllOpponentIds(self, playerID):        opponenetIds= []        firstplayerID = playerID        aOpponentId = self.changePlayer(firstplayerID)        while firstplayerID != aOpponentId:            opponenetIds.append(aOpponentId)            aOpponentId = self.changePlayer(aOpponentId)        return opponenetIds        def heuristic(node,playerId):    # this will evaluate how manyy players are currnt alive ohter then itself    numberOfPlayers = 0    gameBoard = node.state.board    for playerBoard  in gameBoard:        if(gameBoard[playerBoard].isPlayerAlive() and playerId != gameBoard[playerBoard].getId()):             numberOfPlayers +=1    return numberOfPlayersdef lowNumberHeuristic(node,playerId):    passif __name__ == '__main__':    game = GameBoard(4,1)    algo =BestReply()    algo.searchMove(game,2)