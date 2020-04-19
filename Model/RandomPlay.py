import math
from Node import  Node
import random
from Model.Common import *
from copy import deepcopy

node_count = 0
class RandomPlay:

    def __init__(self):
        self.name = "RandomPlay"
        pass

    def __eq__(self, other):
        return self.equals(other)

    def equals(self,other):
        return self.name == other.name
    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def toString(self):
        return self.name

    def searchMove(self,gameState,currentPlayerId):
        allMoves = gameState.generateAllPossibleMoves(currentPlayerId)
        randomMoveIndex = random.randint(0,len(allMoves)-1)
        return allMoves[randomMoveIndex]









