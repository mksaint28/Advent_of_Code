def readArray():

    with open("INPUT.txt", "r") as fileHandler:
        lines = fileHandler.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")
        lines[i] = lines[i].split("\t")
        lines[i] = [int(x) for x in lines[i]]

    return lines

def checkSum(array):
    diff = []
    for i in range(len(array)):
        maxLocal = array[i][0]
        minLocal = array[i][0]
        for j in array[i]:
            if j > maxLocal:
                maxLocal = j
            if j < minLocal and j != 0:
                minLocal = j
        diff.append(maxLocal - minLocal)
    
    return sum(diff)

def evenDivide(array):
    div = []
    for subarr in array:
        maxLocal = max(subarr)
        for x in subarr:
            if maxLocal != x and maxLocal%x == 0:
                div.append(maxLocal/x)
    return sum(div)
# myArray = readArray()

myArray = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]

print(evenDivide(myArray))

# print(checkSum(myArray))
