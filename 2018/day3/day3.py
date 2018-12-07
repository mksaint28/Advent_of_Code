import turtle as t

class claim:

    def __init__(self, name = "EMPTY", lX = 0, lY = 0, width = 0, height = 0):
        self.name = name
        self.lX = lX
        self.lY = lY
        self.width = width
        self.height = height
    

    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName
    
    def getLX(self):
        return self.lX
    
    def setLX(self, pX):
        self.lX = pX

    def getLY(self):
        return self.lY
    
    def setLY(self, pY):
        self.lY = pY
    
    def getRX(self):
        return self.getLX() + self.getWidth()
    
    def getHY(self):
        return self.getLY() + (self.getHeight())

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width
    
    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def description(self):
        return "{0} @ {1},{2}: {3}x{4}".format(self.name, self.lX, self.lY, self.width, self.height)


    def parseClaim(self, string):
        newList = string.split(" ")

        newList.remove("@")

        newList[1] = newList[1].strip(":")
        newList[1] = newList[1].split(",")

        newList[2] = newList[2].split("x")

        self.name = newList[0]

        self.lX = int(newList[1][0])
        self.lY = int(newList[1][1])

        self.width = int(newList[2][0])
        self.height = int(newList[2][1])

        return self


    def overlaps(self, other):
        if (self.getLX() < other.getRX()) and (self.getRX() > other.getLX()) and (self.getHY() > other.getLY()) and (self.getLY() < other.getHY()):
            return True
        
        return False

    def drawClaim(self):

        t.penup()
        t.goto(self.getLX()*10, self.getLY()*10)
        t.pd()
        t.goto(self.getRX()*10, self.getLY()*10)
        t.goto(self.getRX()*10, self.getHY()*10)
        t.goto(self.getLX()*10, self.getHY()*10)
        t.goto(self.getLX()*10, self.getLY()*10)
        t.pu()


# def overlapArea(claim1, claim2):

#     if claim1.getLX < claim2.getRX():
#         newX = claim1.get



myStringList = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
   
myClaimsList = []

for x in myStringList:
    claimHolder = claim()
    myClaimsList.append(claimHolder.parseClaim(x))

for x in myClaimsList:
    print(x.description())
    x.drawClaim()

if (myClaimsList[0].overlaps(myClaimsList[1])):
    print("{} overlaps with {}".format(myClaimsList[0].getName(), myClaimsList[1].getName()))

if (myClaimsList[0].overlaps(myClaimsList[2])):
    print("{} overlaps with {}".format(myClaimsList[0].getName(), myClaimsList[2].getName()))

if (myClaimsList[1].overlaps(myClaimsList[2])):
    print("{} overlaps with {}".format(myClaimsList[1].getName(), myClaimsList[2].getName()))


t.done()
# claim1 = claim(128, 3, 4, 2, 3)