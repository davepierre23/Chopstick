import math
from Node import  Node
from Model.Common import *
from copy import deepcopy

node_count = 0
class Paranoid:

    def __init__(self):
        self.name = "Paranoid"
        pass

    def __eq__(self, other):
        return self.equals(other)

    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def equals(self, other):
        return self.name == other.name

    def toString(self):
        return self.name

    def searchMove(self,gameState,  maximizingPlayerId,depthLimit=2):

        print("Paranoid")
        copyGame = deepcopy(gameState)
        node = Node(copyGame, None, None, 0)
        score, bestNode = self.paranoid(node, depthLimit, maximizingPlayerId, maximizingPlayerId)


        path = get_path(bestNode)
        parent = getParent(bestNode)
        # print("node", node_count)
        # print("parent", parent)
        # print("bestNode", bestNode)
        # print(path)
        global node_count
        node_count = 0
        path.pop(0)
        move = path.pop(0)

        return move





    def paranoid(self,node, depth=0, maximizing_playerId=1, currentPlayerId=1, heuristic=heuristic):

        # count the number of nodes created
        global node_count
        node_count += 1

        if (node.state.cutOff_test(depth)):

            return heuristic(node, currentPlayerId), node

        # if the current player is the maximzing player then its looking for the max value of the score
        if maximizing_playerId == currentPlayerId:
            best_value = -math.inf
            best_node = None
            childNodeList = generateChildState(node, currentPlayerId)

            for childNode in childNodeList:

                goodValue, goodNode = self.paranoid(childNode, depth - 1, maximizing_playerId,childNode.state.changePlayer(currentPlayerId),heuristic)
                # making sure if two states has the same value it just stays with the current best move
                if (best_value != goodValue):
                    best_value = max(best_value, goodValue)
                    # it means that the good move was better and its now currently the best move
                    if goodValue == best_value:
                        best_node = goodNode

            return best_value, best_node
        else:
            best_value = math.inf
            childNodeList = generateChildState(node, currentPlayerId)

            for childNode in childNodeList:

                goodValue, goodNode = self.paranoid(childNode, depth - 1, maximizing_playerId,childNode.state.changePlayer(currentPlayerId),heuristic)
                # making sure if two states has the same value it just stays with the current best move
                if (best_value != goodValue):
                    best_value = min(best_value, goodValue)
                    # it means that the good move was better and its now currently the best move
                    if goodValue == best_value:
                        best_node = goodNode

            return best_value, best_node
