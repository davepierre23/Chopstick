import math
from Node import  Node
from Model.Common import *
from copy import deepcopy


node_count = 0
class BestReply:

    def __init__(self):
        self.name = "BestReply"
        pass

    def __eq__(self, other):
        return self.equals(other)

    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def toString(self):
        return self.name

    def searchMove(self,gameState, currentPlayerID,depthLimit=2):
        print("Best-Reply Algorithem")
        copyGame = deepcopy(gameState)
        node = Node(copyGame, None, None, 0)
        isMaximizingPlayer = True
        score, bestNode = self.best_reply(node, depthLimit, isMaximizingPlayer, currentPlayerID)
        global node_count
        path = get_path(bestNode)
        parent = getParent(bestNode)
        # print("node", node_count)
        # print("bestNode", bestNzxzzzode)
        # print("parent", parent)
        # print(path)
        path.pop(0)
        move = path.pop(0)
        node_count = 0
        return move

    def best_reply(self,node, depth=0, isMaximizing=True, maximizingPlayerID=1, heuristic=heuristic):

        # count the number of nodes created
        global node_count
        node_count += 1

        if (node.state.cutOff_test(depth)):
            return heuristic(node, maximizingPlayerID), node

        else:
            # if the current player is the maximzing player then its looking for the max value of the score
            if isMaximizing:
                best_value = -math.inf
                best_node = None
                childNodeList = generateChildState(node, maximizingPlayerID)

                for childNode in childNodeList:


                    goodValue, goodNode = self.best_reply(childNode, depth - 1, not (isMaximizing), maximizingPlayerID,
                                                     heuristic)
                    # making sure if two states has the same value it just stays with the current best move
                    if (best_value != goodValue):
                        best_value = max(best_value, goodValue)
                        # it means that the good move was better and its now currently the best move
                        if goodValue == best_value:
                            best_node = goodNode

                return best_value, best_node
            else:

                # for all oppoenets do
                # need to implement

                best_value = math.inf

                opponentIds = node.state.getAllOpponentIds(maximizingPlayerID)
                childNodeList = []

                for id in opponentIds:
                    opponentIdChildList = generateChildState(node, id)
                    for child in opponentIdChildList:
                        childNodeList.append(child)

                for childNode in childNodeList:


                    goodValue, goodNode = self.best_reply(childNode, depth - 1, not (isMaximizing), maximizingPlayerID,
                                                     heuristic)
                    # making sure if two states has the same value it just stays with the current best move
                    if (best_value != goodValue):
                        best_value = min(best_value, goodValue)
                        # it means that the good move was better and its now currently the best move
                        if goodValue == best_value:
                            best_node = goodNode

                return best_value, best_node



