# mksaint28
# 11/30/2018
# AoC Day 2

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
        for x in subarr:
            for j in range(len(subarr)):
                if x!=subarr[j] and x%subarr[j] == 0:
                    div.append(x//subarr[j])

    return sum(div)

myArray = readArray()

part1 = checkSum(myArray)
part2 = evenDivide(myArray)

print("The answer to part 1 is {}".format(part1))
print("The answer to part 2 is {}".format(part2))
