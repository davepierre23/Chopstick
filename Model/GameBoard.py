from PlayerHands import PlayerHands
from queue import LifoQueue
from copy import deepcopy

import logging
logging.basicConfig(level=logging.INFO)
import math


node_count = 0


# FFor now is used has the state
class GameBoard:
    HIT = 0
    SPLIT = 1
    def __init__(self, board,  currentIndex=1):
        self.IsGameOver = False  # to see if tis gameover
        self.board = createGameBoard()
        self.currentIndex = currentIndex
        self.childNodes = None
        self.action = None
        self.parent= None


    def __eq__(self, other):
        return self.equals(other)

    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def createGameBoard(self, numberOfPlayers):
        #Game board that has all the player chopstick
        gameBoard= {}
        for playerId in range(1,numberOfPlayers+1):
            gameBoard[i] = PlayerHands(playerId)

        return gameBoard    


    def toString(self):
        return self.board

    def getPlayerHand(playerId):
        return self.board[playerId]

    def equals(self, other):
        # if every piece in the mancala are equal
        return self.board == other.board

    def getPlayerHandAt(self, index):
        return self.board[index]

    def isGameOver(self):

        numberOfAlive = 0
        for playerBoard in self.board:
            if(playerBoard.isPlayerAlive()):
                numberOfAlive += 1
        
        return numberOfAlive == 1 


        

    def getWinner(self):
        if(self.isGameOver()):
        
            for playerBoard in self.board:
                if(playerBoard.isPlayerAlive()):
                    print("The winner pf the game is player Id", playerBoard.getId())
                    return playerBoard
            
        print("There was not any winner")


    def generateAllPossibleMoves(self,playerId):

        moveList = []
        hitMoves = self.generateHitPossibleMoves(playerId)

        for move in hitMoves:
            moveList.append(move)

           
        #for now can split at anytime but cant be the same pair 
        splitMoves = self.generateSplitPossibleMoves(playerId)
        for move in splitMoves:
             moveList.append(move)

        
        return 



    def generateSplitPossibleMoves(self,playerId):

        #get playerBoard
        playerBoard = getPlayerHand(playerId)

        #
        totalNumSticks = 0 

        leftHandNum = playerBoard.getNumOfStickLeftHand()
        rightHandNum = playerBoard.getNumOfStickRightHand()
        totalNumSticks += leftHandNum
        totalNumSticks += rightHandNum

        # generate all the possible ways to split 
        moveList = []
        for i in range(1,totalNumSticks):
            leftHand = i 
            rightHand = totalNumSticks - i
            if((leftHandNum != leftHand and rightHandNum != rightHand) or (leftHandNum != rightHand and rightHandNum != leftHand)  ):
                aMove=[]
                aMove.append(self.SPLIT)
                aMove.append(leftHand)
                aMove.append(rightHand)
                print("number on the left hand", leftHand )
                print("number on the right hand", rightHand -i )
                moveList.append(aMove)



            


        #TODO: get rid of duplicates
        #no 1 6 and 6 1

        return moveList

    def generateHitPossibleMoves(self,playerId, move):


        moveList = []
        playerTurn = getPlayerHand(playerId)
        for playerBoard in self.board:
            # if the player does not have the same player ID has the playerBoard
            if(playerId != playerBoard.getId()):
                if(playerTurn.isLeftHandAlive()):
                    leftToAttackChoice = playerTurn.LEFT
                    leftHitMove = []
                    leftHitMove.append(self.HIT) # HIT or SPLIT 0 index
                    leftHitMove.append(leftToAttackChoice) # choice hand of had to hit with 1 index
                    playerIdToHit = playerBoard.getId()
                    leftHitMove.append(playerIdToHit)  # playerID to hit with 2 index 

                    # playerHand index 3


                    # left hand hits the left hand of the other if both are alive
                    if(playerBoard.isLeftHandAlive()):
                        
                        aMove = deepcopy(leftHitMove)
                        aMove.append(playerBoard.LEFT) 
                        moveList.append(aMove)

                    # left hand hits the right of the other if both are alive 
                    if(playerBoard.isRightHandAlive()):
                        aMove = deepcopy(leftHitMove)
                        aMove.append(playerBoard.RIGHT)
                        moveList.append(aMove)

                    
                    
                if(playerTurn.isRightHandAlive()):
                    rightToAttackChoice = playerTurn.RIGHT
                    rightHitmove = []
                    rightHitmove.append(self.HIT)
                    rightHitmove.append(rightToAttackChoice)
                    playerIdToHit = playerBoard.getId()
                    rightHitmove.append(playerIdToHit)


                    # right hand hits the left hand of the other if both are alive
                    if(playerBoard.isLeftHandAlive()):
                        aMove = deepcopy(rightHitmove)
                        aMove.append(playerBoard.LEFT)
                        moveList.append(aMove)

                    # right hand hits the right hand of the other player
                    if(playerBoard.isRightHandAlive()):
                        aMove = deepcopy(rightHitmove)
                        aMove.append(playerBoard.RIGHT)
                        moveList.append(aMove)
                    



        return moveList


    def applySplitChoice(self,playerId,move):
        playerBoard = getPlayerHand(playerId)

        leftHand = move[1]
        rightHand = move[2]

        playerBoard.setNumOfStickLeftHand(leftHand)
        playerBoard.setNumOfStickRightHand(rightHand)

    def applyHitChoice(self,playerId,move):
        playerBoard = getPlayerHand(playerId)

        currentPlayerHandChoice = move[1]
        playerHandChoiceNumber = playerBoard.getHandOfChoice(currentPlayerHandChoice)

        playerHandToHit = getPlayerHand(move[2])
        oppHand = move[1]
        playerHandToHit.hit(oppHand,playerHandChoiceNumber)




    def isSplitMove(self, move):
        return move[0] == self.SPLIT
    
    def isHitMove(self, move):
        return move[0] == self.HIT


    def make_move(self,currentPlayerId):
        if (self.isGameOver()):
            return

        currentPlayerId = currentPlayerId

        # if player is a human
        moves = self.getStaringMove()

        # if the move was SPLIT move 
        if (self.isSplitMove(move)):
            self.applySplitChoice(playerId,move)
        
            
        else:
           # if it was a hit move 
           self.applyHitChoice(playerId, move) 
       
      

    def cutOff_test(self, depth):
        return self.isGameOver() or depth == 0

    def flipPlayer(self, playerId):
        if playerId == 1:
            return 2
        else:
            return 1
    def heuristic(self,playerId):
        # this will evaluate how manyy players are currnt alive ohter then itself
        numberOfPlayers = 0
        for playerBoard  in self.board:
            if(playerBoard.isPlayerAlive() and playerId != playerBoard.getId()):
                numberOfPlayers +=1

        return numberOfPlayers


    def mini_max(self, depth=0, maximizing_player=False, playerId=1):
        global node_count
        node_count += 1


        if (self.cutOff_test(depth)):
            return self.heuristic(playerId), self

        if maximizing_player:
            best_value = -math.inf
            best_move = None
            moves, succesorsStates = beginGeneratingAllMoves(self.board, playerId)

            for (move, childState) in zip(moves, succesorsStates):
                logging.debug(move)
                #printBoard(childState)

                childState.parent = self
                childState.action = move
                goodValue, goodMove= childState.mini_max(depth - 1, not maximizing_player, self.flipPlayer(playerId))
                # making sure if two states has the same value it just stays with the current best move
                if (best_value != goodValue):
                    best_value = max(best_value, goodValue)
                    # it means that the good move was better and its now currently the best move
                    if goodValue == best_value:
                        best_move = goodMove
            return best_value, best_move
        else:
            best_value = math.inf
            moves, succesorsStates = beginGeneratingAllMoves(self.board, playerId)

            for (move, childState) in zip(moves, succesorsStates):
                #print(move)
                #printBoard(childState)

                childState.parent = self
                childState.action = move
                goodValue, goodMove= childState.mini_max(depth - 1, not maximizing_player, self.flipPlayer(playerId))
                # making sure if two states has the same value it just stays with the current best move
                if (best_value != goodValue):
                    best_value = min(best_value, goodValue)
                    # it means that the good move was better and its now currently the best move
                    if goodValue == best_value:
                        best_move = goodMove

            return best_value, best_move
    def mini_max_alpha_beta(self, depth=0, maximizing_player=False, playerId=1,  alpha= - 1000000000, beta=1000000000, heur =1):
        global node_count
        node_count += 1


        if (self.cutOff_test(depth)):
            if(heur==2):
                return self.heuristic2(playerId), self
            else:
                return self.heuristic1(playerId), self

        if maximizing_player:
            best_value = -math.inf
            best_move = None
            moves, succesorsStates = beginGeneratingAllMoves(self.board, playerId)

            for (move, childState) in zip(moves, succesorsStates):
                logging.debug(move)
                #printBoard(childState)

                childState.parent = self
                childState.action = move
                goodValue, goodMove= childState.mini_max_alpha_beta(depth - 1, not maximizing_player, self.flipPlayer(playerId), alpha, beta, heur)
                # making sure if two states has the same value it just stays with the current best move
                if (best_value != goodValue):
                    best_value = max(best_value, goodValue)
                    alpha = max(alpha,goodValue)
                    # it means that the good move was better and its now currently the best move
                    if goodValue == best_value:
                        best_move = goodMove

                if(beta <= alpha):
                    break


            return best_value, best_move
        else:
            best_value = math.inf
            moves, succesorsStates = beginGeneratingAllMoves(self.board, playerId)

            for (move, childState) in zip(moves, succesorsStates):
                logging.debug(move)
                #printBoard(childState)

                childState.parent = self
                childState.action = move
                goodValue, goodMove= childState.mini_max_alpha_beta(depth - 1, not maximizing_player, self.flipPlayer(playerId), alpha, beta,heur)
                # making sure if two states has the same value it just stays with the current best move
                if (best_value != goodValue):
                    best_value = min(best_value, goodValue)
                    beta = min(beta, goodValue)
                    # it means that the good move was better and its now currently the best move
                    if goodValue == best_value:
                        best_move = goodMove

                    if (beta <= alpha):
                        break


            return best_value, best_move



def explorePossibleStates(initState, moves, playerId):

    logging.debug("Starting Depth First Search")
    nodeList = LifoQueue()

    for dir, holeToScoop in (moves):
        newState = deepcopy(initState)
        newState.dir = dir
        newState.scoopHole(holeToScoop)
        newState.currentIndex = holeToScoop
        node = Node(newState, None, [dir, holeToScoop], 1, 0)
        nodeList.put(node)
        logging.debug("Init State")
        logging.debug(str(newState))


    moves = []


    states = []

    while (not(nodeList.empty())):
        e = nodeList.get()
        logging.debug("Currently exploring this state: " + e.state.toString())
        #need to change for the game to AllPossibleActions
        e.state.make_move(playerId)
        if(not(e.state.childNodes == None)):
            logging.debug("Exploring childNodes")
            logging.debug("Len of nodes Explored " + str(len(nodeList.queue)))
            for newState in e.state.childNodes :
                node = Node(newState, e,newState.action,  e.pathCost+1 , e.depth+1)
                nodeList.put(node)
        else:
            logging.debug("Len of nodes Explored " + str(len(nodeList.queue)))
            logging.debug("No more decisions")
            path = get_path(e)
            logging.debug(len(path))
            logging.debug(path)


            moves.append(path)
            e.state.action = path
            states.append(e.state)


    logging.debug("Moves list", str(moves) + "\n number of moves" + str(len(moves)))
    return moves , states






def beginGeneratingAllMoves(board, playerId):

    #24 array to be copied
    newboard = deepcopy(board)

    #create a state
    initState = SimulatedBoard(newboard)

    #get all possible starting moves
    moves= initState.generateAllStartingMoves(playerId)

    return explorePossibleStates(initState,moves,playerId)
def miniMax(board,playerId,depth=2):
    # 24 array to be copied
    print("IntialState")

    newboard = deepcopy(board)

    # create a state
    intialState = SimulatedBoard(newboard)
    #printBoard(intialState)

    score, moves = intialState.mini_max(depth,True,playerId)
    print("MiniMax Results")
    print("score",score)
    global node_count
    print("node", node_count)
    node_count = 0
    move = getParent(moves).pop(1).action
    print("action", move)


    return move

def paranoid(game,playerId,depth=2):
    print("Paranoid")

    copyGame = deepcopy(game)
    # create a state
    intialState = SimulatedBoard(newboard)
    #printBoard(intialState)

    score, moves = intialState.mini_max(depth,True,playerId)
    print("MiniMax Results")
    print("score",score)
    global node_count
    print("node", node_count)
    node_count = 0
    move = getParent(moves).pop(1).action
    print("action", move)


    return move


def miniMaxAlphaBeta(board,playerId, depth=2):
    # 24 array to be copied
    print("Starting Aplha Beta search")
    newboard = deepcopy(board)

    # create a state
    intialState = SimulatedBoard(newboard)
    #printBoard(intialState)

    score, moves = intialState.mini_max_alpha_beta(depth,True,playerId, heur =playerId)
    print("AlphaBeta Results:")

    moves = getParent(moves)
    if(len(moves)>1):

        move= moves.pop(1).action
        print("action", move)
    else:
        print(moves)
        moves , states = beginGeneratingAllMoves(board,playerId)
        move = moves[0]
        print()




    global node_count
    print("node", node_count)
    node_count = 0

    print("Ending search ")
    return move


def get_path(node):
    node
    path = []
    path.insert(0, node.action)
    parent = node.parent
    while parent:
        path.insert(0, parent.action)
        parent = parent.parent

    return path

def getParent(node):
    node
    path = []
    parent = node.parent
    while parent:
        path.insert(0, parent)
        parent = parent.parent

    return path


if __name__ == '__main__':
    pass


``
