def read_input():
    with open("INPUT.txt", "r") as f:
        theInput = f.readlines()
    
    return theInput


def stripNewLines(aList):

    for i in range(len(aList)):
        aList[i] = aList[i].strip("\n")
    
    return aList


myInputList = read_input()

stripNewLines(myInputList)

myInputList.sort()

print(myInputList)