import math
from Node import  Node
from Model.Common import *
from copy import deepcopy


node_count = 0
class Max_n:

    def __init__(self):
        self.name = "Max-n"
        pass

    def __eq__(self, other):
        return self.equals(other)

    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def toString(self):
        return self.name


    def searchMove(self,gameState, currentPlayerId,depthLimit=2):
        print("Max-N")
        copyGame = deepcopy(gameState)
        node = Node(copyGame, None, None, 0)
        score, bestNode = self.max_n(node, depthLimit, currentPlayerId)
        global node_count
        path = get_path(bestNode)
        parent = getParent(bestNode)
        # print("node", node_count)
        # print("bestNode", bestNode)
        # print("parent", parent)
        # print(path)
        path.pop(0)
        move = path.pop(0)
        node_count = 0
        return move



    def max_n(self,node, depth=0, currentPlayerId=1, heuristic=heuristic):
        # count the number of nodes created
        global node_count
        node_count += 1

        if (node.state.cutOff_test(depth)):
            return self.createTuple(node, heuristic), node

        # if the current player is the maximzing player then its looking for the max value of the score
        else:

            best_value = -math.inf
            scoresOfAll = []
            best_node = None
            childNodeList = generateChildState(node, currentPlayerId)

            for childNode in childNodeList:
                aScoreTuple, goodNode = self.max_n(childNode, depth - 1, childNode.state.changePlayer(currentPlayerId),heuristic)
                # making sure if two states has the same value it just stays with the current best move
                if (best_value != aScoreTuple):
                    best_value = max(best_value, aScoreTuple[currentPlayerId])

                    # it means that the good move was better and its now currently the best move
                    if aScoreTuple[currentPlayerId] == best_value:
                        scoresOfAll = aScoreTuple
                        best_node = goodNode

            return scoresOfAll, best_node


    def createTuple(self,node, heuristic):
        # Game board that has all the player chopstick

        gameState = node.state
        scoreTuple = {}
        for playerId in (gameState.board):
            scoreTuple[playerId] = heuristic(node, playerId)

        return scoreTuple
