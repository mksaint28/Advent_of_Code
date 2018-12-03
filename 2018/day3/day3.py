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
    
    def getRY(self):
        return self.getLY() + self.getHeight()

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


    def compareOverlap(self, other):
        if (self.getLX() > other.getRX()) or (other.getLX() > self.getRX()):
            return False
        
        if (self.getLY() < other.getRY()) or (other.getLY() < self.getRY()):
            return False

        return True
        

myStringList = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
   
myClaimsList = []

for x in myStringList:
    claimHolder = claim()
    myClaimsList.append(claimHolder.parseClaim(x))

for x in myClaimsList:
    print(x.description())

if (myClaimsList[0].compareOverlap(myClaimsList[1])):
    print("{} overlaps with {}".format(myClaimsList[0].getName(), myClaimsList[1].getName()))

if (myClaimsList[0].compareOverlap(myClaimsList[2])):
    print("{} overlaps with {}".format(myClaimsList[0].getName(), myClaimsList[2].getName()))

if (myClaimsList[1].compareOverlap(myClaimsList[2])):
    print("{} overlaps with {}".format(myClaimsList[1].getName(), myClaimsList[2].getName()))

# claim1 = claim(128, 3, 4, 2, 3)