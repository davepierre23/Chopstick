from Model.Node import Node
from queue import LifoQueue
from copy import deepcopy
import logging
logging.basicConfig(level=logging.INFO)
import time

class Search():

    def __init__(self,initState):
        self.name = "DFS"
        self.initState = initState
        self.goalNode = None
        self.numOfVistedNodes = 0
        self.search()
        self.dfs_path()

    def __str__(self):
        isSucess = self.isSuceesful()
        sucessOrFail = ""
        if(isSucess):
            sucessOrFail = "SUCESS"
        else:
            sucessOrFail = "FAIL"

        return self.name + "-"+str(sucessOrFail)+": pathLength="+ str(len(self.path))+ " \n"+ "path = "+ str(self.path) + " \n"+ "num of Explore Node = "+ str(self.numOfVistedNodes)

    def search(self):

        logging.debug("Starting Search")

        node = Node(self.initState,None,self.initState.cats.getCoordinate(),1,0)
  

        
        visited = set()

        while(not(goal) and not(nodeList.empty())):
            e = nodeList.get()
            logging.debug("Currently exploring this state: "+ e.state.toString())

            if e.state not in visited :
                logging.debug("Adding this state to visted")
                visited.add(e.state)

                childNodes = self.expand(e)

                logging.debug("Checking child nodes if they are the goal")

                for childNode in childNodes:
                    if childNode.state.isGoal():
                        logging.debug("Current state is the goal" + childNode.state.toString())
                        numOfVistedNodes=len(visited)
                        logging.debug("Number of explored node for depth search is "+ str(numOfVistedNodes))
                        goal = True
                        self.goalNode = childNode
                        self.numOfVistedNodes = numOfVistedNodes
                        return childNode, numOfVistedNodes
                        break
                    else:
                        childNode.state.mouses.move()
                        logging.debug("The State to be added to the queue" + childNode.state.toString())
                        nodeList.put(childNode)
            else:
                logging.debug("I have visted this state")

        
        return nodeList
    def expand(self,node):
        succesors = []

        possibleMoves = node.state.possibleActions()

        for move in possibleMoves:

            newState = deepcopy(node.state)
            newState.executeAction(move)
            childNode =Node(newState, node, move, node.f, node.depth +1)
            succesors.append(childNode)

        return succesors
    def isSuceesful(self):
        return not (self.goalNode is None)
    def dfs_path(self):
        if  self.isSuceesful():
            node = self.goalNode
            path = []
            path.insert(0, node.action)
            parent= node.parent
            while parent:
                path.insert(0, parent.action)
                parent = parent.parent
            path.pop(0)
            self.path = path

            return path

        else:
            self.path = []

    def getResult(self):
        searchName = self.name
        numofExploredNodes = self.numOfVistedNodes
        numOfMoves = len(self.path)
        numOfMouse = self.initState.mouses.numOfSteps
        return searchName, numOfMouse,numofExploredNodes , numOfMoves


def runParanoidAlgo(gameState):
     node = Node(gameState,None,self.initState.cats.getCoordinate(),1,0)


def paranoid(node, depth=0, maximizing_player=1, currentPlayer=1):
        
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


