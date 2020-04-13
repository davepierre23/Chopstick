

# FFor now is used has the state
class SimulatedBoard:
    def __init__(self, board, hand=0, currentIndex=-1, dir=-1):
        self.IsGameOver = False  # to see if tis gameover
        self.board = board
        self.mancalaOpposite = dict({0: 6, 6: 0, 12: 18, 18: 12})
        self.middleHolesIndex = [3, 9, 15, 21]
        self.dir = dir
        self.startingHole =-1
        self.hand = hand
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


    def toString(self):
        strArray = []
        for piece in range(len(self.board)):
            strArray.append(str(self.board[piece]))

        return str(strArray) + "\n " + " hand num" + str(self.hand) +  "CurrentIndex:" + str(self.currentIndex) + "DIR: " + str(self.dir)

    def equals(self, other):
        # if every piece in the mancala are equal
        isEqual = True
        for i in range(len(self.board)):
            if (self.board[i] != self.other.board[i]):
                isEqual = False

        return isEqual

    def getBoardAt(self, index):
        return self.board[index]


    def isGameOver(self):
        # will count every piece that not mancala and if one side has stones stones return true else false
        numOfP1Stones = 0
        numOfP2Stones = 0
        for i in range(len(self.board)):
            if (self.board[i].isPlayerPiece(1) and isinstance(self.board[i], Hole)):
                numOfP1Stones += self.board[i].getNumOfStones()
            elif (self.board[i].isPlayerPiece(2) and isinstance(self.board[i], Hole)):
                numOfP2Stones += self.board[i].getNumOfStones()
        # print("The number of stones that P1 has ", numOfP1Stones)
        # print("The number of stones that P2 has ", numOfP2Stones)
        value = numOfP1Stones == 0 or numOfP2Stones == 0
        # print("Result", value)
        return value

    def getWinner(self):
        # will be trigger when its game over
        # will count every piece that not mancala and if one side has stones stones return true else false
        numOfP1Stones = 0
        numOfP2Stones = 0
        for i in range(len(self.board)):
            if (self.board[i].isPlayerPiece(1)):
                numOfP1Stones += self.board[i].getNumOfStones()
            elif (self.board[i].isPlayerPiece(2)):
                numOfP2Stones += self.board[i].getNumOfStones()

        if (numOfP1Stones > numOfP1Stones):
            logging.debug("P1 wins")
        elif (numOfP1Stones < numOfP2Stones):
            logging.debug("P2 wins")

        else:
            logging.debug("It's Draw ")


    def choosePlaceHolderToPick(self, playerId):
        # return the list of avaiable holes to pick from from therre id
        options = []
        for i in range(len(self.board)):
            if (self.board[i].isPlayerPiece(playerId) and self.board[i].getNumOfStones() > 0 and isinstance(
                    self.board[i], Hole)):
                options.append(self.board[i].getId())

        return options

    def generateAllStartingMoves(self,playerId):
        CLOCKWISE= 1
        COUNTERCLOCKWISE =2

        pieceOptions = self.choosePlaceHolderToPick(playerId)

        startingMoveAndDir = []

        for option in (pieceOptions):
            startingMoveAndDir.append([CLOCKWISE,option])
            # startingMoveAndDir.append([COUNTERCLOCKWISE,option])
            # break


        logging.debug(startingMoveAndDir)
        return startingMoveAndDir

    def scoopHole(self, holeNumber):
        # pick up  all the stones at the hole number
        self.hand = 0
        self.hand += self.board[holeNumber].getNumOfStones()
        self.board[holeNumber].setNumOfStones(0)

        return self.hand

    def makeChoiceOppMancala(self, oppMancala):
        SKIP = 0
        GIVEONETAKEONE = 1
        GIVEONETAKETWO = 2

        optionsAvailable = []
        optionsAvailable.append(SKIP)
        if (oppMancala.getNumOfStones() >= 1):
            optionsAvailable.append(GIVEONETAKEONE)

        if (oppMancala.getNumOfStones() >= 2):
            optionsAvailable.append(GIVEONETAKETWO)

        return optionsAvailable


    def applyChoiceOppMancala(self, oppMancala, choice, hand):
        SKIP = 0
        GIVEONETAKEONE = 1
        GIVEONETAKETWO = 2

        if (GIVEONETAKEONE == choice):
            # steal a stone
            oppMancala.removeStones(1)
            self.hand -= 1

            # adding the stolen stones to the player mancala
            playerOppositeMancala = self.mancalaOpposite[oppMancala.getId()]
            self.getBoardAt(playerOppositeMancala).addStone(1)
            logging.debug("GIVEONETAKEONE")

        elif (GIVEONETAKETWO == choice):
            # steal a stone
            oppMancala.removeStones(2)
            self.hand -=1

            # adding the stolen stones to the player mancala
            playerOppositeMancala = self.mancalaOpposite[oppMancala.getId()]
            self.getBoardAt(playerOppositeMancala).addStone(2)
            logging.debug("GIVEONETAKETWO")


        elif (choice == SKIP):
            logging.debug("SKIP")

        return self.hand

    def drop(self, holeNumber):
        self.board[holeNumber].addStone()

    # Our Heuristic1 Count how many rocks on his pieces
    def heuristic1(self, playerId):
        score = 0
        for i in range(len(self.board)):
            if (self.board[i].isPlayerPiece(playerId)):
                score += self.board[i].getNumOfStones()
        return score

    # Our Heuristic2  counts how many are in his mancala
    def heuristic2(self, playerId):
        score = 0
        for i in range(len(self.board)):
            if (self.board[i].isPlayerPiece(playerId) and isinstance(self.board[i], Mancala)):
                score += self.board[i].getNumOfStones()
        return score

    def getNextPieceIndex(self, index, dir=1):
        CLOCKWISE = 1
        COUNTERCLOCKWISE = 2
        # will
        if (dir == CLOCKWISE):
            index += 1

            # we went over too much
            if index == 24:
                index = 0

        elif (dir == COUNTERCLOCKWISE):
            index -= 1

            # too little
            if index == -1:
                index = 23

        return index



    def makeChoiceMiddleHoles(self, nextBoardPiece):
        # Create a dictionary of the middle holes adjacent
        middleHolesAjacentOptions = dict({3: [9, 21], 9: [3, 15], 15: [9, 21], 21: [3, 15]})

        # get the  id of the next BoardPiece and place it in the
        options = middleHolesAjacentOptions[nextBoardPiece.getId()]

        return options



    def applyChoiceMiddleHoles(self, option, currentPlayerId):

        boardPiece = self.board[option]

        numOfStonesStolen = boardPiece.getNumOfStones()
        boardPiece.removeStones(boardPiece.getNumOfStones())

        # add the stolen stones to the closest mancala
        index = option
        CLOCKWISE = 1
        COUTERCLOCKWISE = 2
        hasFoundClosestMancala = False

        nextHoleIndexByCw = self.getNextPieceIndex(index, CLOCKWISE)
        nextHoleIndexByCCw = self.getNextPieceIndex(index, COUTERCLOCKWISE)

        # until we find the closest mancala to update increate the index
        while (not (hasFoundClosestMancala)):
            # if the cloest player mancala is clockwise then add the stones
            if (self.board[nextHoleIndexByCw].isPlayerPiece(currentPlayerId) and isinstance(
                    self.board[nextHoleIndexByCw], Mancala)):
                hasFoundClosestMancala = True
                mancalaToAddStones = self.board[nextHoleIndexByCw]

            # if the cloest player mancala is counterclockWise then add the stones
            elif (self.board[nextHoleIndexByCCw].isPlayerPiece(currentPlayerId) and isinstance(
                    self.board[nextHoleIndexByCCw], Mancala)):
                hasFoundClosestMancala = True
                mancalaToAddStones = self.board[nextHoleIndexByCw]

            # check the next boardPiece in that direction
            nextHoleIndexByCw = self.getNextPieceIndex(nextHoleIndexByCw, CLOCKWISE)
            nextHoleIndexByCCw = self.getNextPieceIndex(nextHoleIndexByCCw, COUTERCLOCKWISE)

        # add the mancala stones that we stole
        mancalaToAddStones.addStone(numOfStonesStolen)

    def getStaringMove(self):
        return self.dir, self.currentIndex

    

    def make_move(self,currentPlayerId):
        if (self.isGameOver()):
            return

        currentPlayerId = currentPlayerId

        # if player is a human
        DIR, holeNumber = self.getStaringMove()




        # direction will be clockwise  for now

        index = holeNumber
        while (self.hand > 0):


            nextHoleIndex = self.getNextPieceIndex(index, DIR)

            nextBoardPiece = self.getBoardAt(nextHoleIndex)


            # if the gamePiece is Mancala and its their oppoenent :
            if (not (nextBoardPiece.isPlayerPiece(currentPlayerId)) and isinstance(nextBoardPiece, Mancala)):


                options = self.makeChoiceOppMancala(nextBoardPiece)
                childNodes = []
                for option in range(len(options)):
                    newState = deepcopy(self)
                    newState.action = option
                    newState.applyChoiceOppMancala(nextBoardPiece, option, self.hand)
                    childNodes.append(newState)


                self.childNodes = childNodes


            # if the next drop is the last one and its in its own mancala call make makeMove again
            elif (self.hand == 1 and nextBoardPiece.isPlayerPiece(currentPlayerId) and isinstance(nextBoardPiece, Mancala)):
                self.hand -= 1
                self.drop(nextHoleIndex)

                moves = self.generateAllStartingMoves(currentPlayerId)
                childNodes = []

                for dir, holeToScoop in moves:
                    newState = deepcopy(self)
                    newState.action = [dir,holeToScoop]
                    newState.dir = dir
                    newState.scoopHole(holeToScoop)
                    newState.currentIndex = holeToScoop
                    childNodes.append(newState)

                self.childNodes = childNodes



            # do last if statement of if its the special thing
            elif (self.hand == 1 and nextBoardPiece.isPlayerPiece(currentPlayerId) and (nextBoardPiece.getId() in self.middleHolesIndex) and nextBoardPiece.getNumOfStones() ==0):

                self.hand -= 1
                self.drop(nextHoleIndex)
                options = self.makeChoiceMiddleHoles(nextBoardPiece)
                childNodes = []
                for option in options:
                    newState = deepcopy(self)
                    newState.action = option
                    newState.applyChoiceMiddleHoles(option,currentPlayerId)
                    childNodes.append(newState)

                self.childNodes = childNodes


            else:
                logging.debug("Board After dropping at Index" , nextHoleIndex)
                self.drop(nextHoleIndex)
                self.hand -= 1

            index = nextHoleIndex

    def cutOff_test(self, depth):
        return self.isGameOver() or depth == 0

    def flipPlayer(self, playerId):

        if playerId == 4:
            return 1
        else:
            return playerId +1

    def paranoid(self, depth=0, maximizing_player=1, currentPlayer=1):
        
        # count the number of nodes created
        global node_count
        node_count += 1

        if (self.cutOff_test(depth)):
            return self.heuristic2(playerId), self

        # if the current player is the maximzing player then its looking for the max value of the score
        if maximizing_player == currentPlayer:
            best_value = -math.inf
            best_move = None
            moves, succesorsStates = beginGeneratingAllMoves(self.board, playerId)

            for (move, childState) in zip(moves, succesorsStates):
                logging.debug(move)
                #printBoard(childState)

                childState.parent = self
                childState.action = move
                goodValue, goodMove= childState.paranoid(depth - 1, maximizing_player, self.flipPlayer(playerId))
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
                goodValue, goodMove= childState.paranoid(depth - 1, not maximizing_player, self.flipPlayer(playerId))
                # making sure if two states has the same value it just stays with the current best move
                if (best_value != goodValue):
                    best_value = min(best_value, goodValue)
                    # it means that the good move was better and its now currently the best move
                    if goodValue == best_value:
                        best_move = goodMove

            return best_value, best_move

    def max_n(self, depth=0,currentPlayer=1):
        
        # count the number of nodes created
        global node_count
        node_count += 1

        if (self.cutOff_test(depth)):
            return self.heuristic2(currentPlayer), self

        else:
            best_value = -math.inf
            all_score = []
            best_move = None
            moves, succesorsStates = beginGeneratingAllMoves(self.board, currentPlayer)

            for (move, childState) in zip(moves, succesorsStates):
                logging.debug(move)
                #printBoard(childState)

                childState.parent = self
                childState.action = move
                goodValue, goodMove= childState.max_n(depth - 1, self.flipPlayer(currentPlayer))

                # making sure if two states has the same value it just stays with the current best move
                if (best_value != goodValue):
                    best_value = max(best_value, goodValue[currentPlayer])
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



if __name__ == '__main__':
    boad = Board(1)

    #miniMaxAlphaBeta(boad.board, 2,4)
    miniMax(boad.board,2,4)





