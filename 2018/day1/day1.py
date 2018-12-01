def read_input():
    with open("./2018/day1/INPUT.txt", "r") as f:
        theInput = f.read()
    
    return theInput

def str_2_arr(aString):
    aString = aString.split("\n")

    return aString

def str_2_int(stringArray):
    arrOut = []
    for i in range(len(stringArray)):
        arrOut.append(int(stringArray[i]))
    
    return arrOut

def totalSum(list, offset):
    return sum(list) + offset

def freqCheck(list):
    freqs = [0]
    mySum = 0
    check = True

    while check:
        for i in list:
            mySum+= i
            if mySum not in freqs:
                freqs.append(mySum)
            else:
                check = False
                break
    
    return mySum

rawString = read_input()

stringArr = str_2_arr(rawString)

intArr = str_2_int(stringArr)

part1 = totalSum(intArr, 0)

part2 = freqCheck(intArr)

print(part1)

print(part2)