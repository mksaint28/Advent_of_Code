#Offset double addition

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

with open("INPUT.txt", "r") as file_handler:
    theInput = file_handler.read()

print(samesies(theInput, int(len(theInput)/2)))