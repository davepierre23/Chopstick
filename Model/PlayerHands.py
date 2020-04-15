

# FFor now is used has the state
class PlayerHands:
    LEFT = 0
    RIGHT = 1
    LIMIT =10
    def __init__(self,id):
        self.id = id
        self.choperStickHolder = [1,1]

        #index 0 is number on left and
        # index 1 is number on right 



    def __eq__(self, other):
        return self.equals(other)

    def __str__(self):
        return self.toEasierString()

    def __repr__(self):
        return self.toEasierString()


    def toString(self):
        return  "ID = " + str(self.id)+ "\nNumber of chopsticks on the left " + str(self.choperStickHolder[self.LEFT]) +   "\n Number of chopsticks on the right " + str(self.choperStickHolder[self.RIGHT])

    def toEasierString(self):
        return  "ID = " + str(self.id)+ " :" + str(self.choperStickHolder)

    def equals(self, other):
        return self.id == other.id

    def getId(self):
        return self.id

    def getNumOfStickLeftHand(self):
        return self.choperStickHolder[self.LEFT]
    
    def getNumOfStickRightHand(self):
        return self.choperStickHolder[self.RIGHT]
    
    def getHandOfChoice(self,handChoice):
        if(handChoice == self.LEFT):
            return self.getNumOfStickLeftHand()
        if(handChoice == self.RIGHT):
            return self.getNumOfStickRightHand()
      
    
    #will now be the roll over variation where have more then 10 goes back to 1 
    def hit(self,handChoice,numOfSticks):
        if(handChoice == self.LEFT):
            updatedSticks = self.getNumOfStickLeftHand() + numOfSticks
            updatedSticks = updatedSticks % self.LIMIT
            self.setNumOfStickLeftHand(updatedSticks)


        else:
            if(handChoice == self.RIGHT):
                updatedSticks = self.getNumOfStickRightHand() + numOfSticks
                updatedSticks = updatedSticks % self.LIMIT
                self.setNumOfStickRightHand(updatedSticks)



    def isLeftHandAlive(self):
        return self.choperStickHolder[self.LEFT] > 0

    def isRightHandAlive(self):
        return self.choperStickHolder[self.RIGHT] > 0
    def isPlayerAlive(self):
        return self.isLeftHandAlive() or self.isRightHandAlive()

    def setNumOfStickLeftHand(self, numSticks):
        self.choperStickHolder[self.LEFT] = numSticks
    
    def setNumOfStickRightHand(self, numSticks):
        self.choperStickHolder[self.RIGHT] = numSticks
    
if __name__ == "__main__":
    playerBoard = PlayerHands(2)
    print(playerBoard)
    playerBoard.hit(1,9)
    print(playerBoard.getHandOfChoice(1))
    print(playerBoard)
