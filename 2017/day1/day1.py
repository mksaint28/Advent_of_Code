# mksaint28
# 11/30/2018
# AoC Day 1

def readIn():
    with open("INPUT.txt", "r") as file_handler:
        theInput = file_handler.read()

    return theInput

def samesies(numbers, offset):

    theSum = 0

    for i in range(len(numbers)):

        try:
            if numbers[i] == numbers[i + offset]:
                theSum += int(numbers[i])
    
        except IndexError:
            if numbers[i] == (numbers[i - offset]):
                theSum += int(numbers[i])

    return theSum

myList = readIn()

part1 = samesies(myList, 1)
part2 = samesies(myList, len(myList)//2)

print("The answer to part 1 is {}".format(part1))
print("The answer to part 2 is {}".format(part2))
