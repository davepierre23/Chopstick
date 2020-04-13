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

        logging.debug("Starting Depth First Search")

        node = Node(self.initState,None,self.initState.cats.getCoordinate(),1,0)
        if (node.state.isGoal()):
            logging.debug("Goal has been reached")
            return node


        goal= False
        nodeList = LifoQueue()
        nodeList.put(node)

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

        self.goalNode = None
        self.numOfVistedNodes = len(visited)
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



