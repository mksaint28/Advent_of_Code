def readIn():
    with open("INPUT.txt", "r") as f:
        lines = f.readlines()
        lines = [x.strip("\n") for x in lines]

    return lines

# Part1
def scoreString2(myString):
    for x in myString:
        if myString.count(x) == 2:
            return 1
    
    return 0


def scoreString3(myString):
    for x in myString:
        if myString.count(x) == 3:
            return 1
    
    return 0


def scoreList(listIn):
    twoCount = 0
    threeCount = 0

    for x in listIn:
        twoCount += scoreString2(x)
        threeCount += scoreString3(x)
    
    return twoCount * threeCount


# Part 2
def checkString(string1, string2):
    checkNum = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            checkNum += 1
    
    if checkNum == 1:
        return True

    return False


def checkID(myList):

    for x in myList:
        for i in range(1, len(myList)):
            if checkString(x, myList[i]):
                return [x, myList[i]]
    
    return 0


def removeDiff(string1, string2):

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return string1[0:i] + string2[i+1:len(string2)]


theInput = readIn()

part1 = scoreList(theInput)

resultList = checkID(theInput)

if resultList != 0:
    part2 = removeDiff(resultList[0], resultList[1])

else:
    part2 = "Oops! Something went wrong :("

print("The answer to part 1 is: {}".format(part1))

print("The answer to part 2 is: {}".format(part2))