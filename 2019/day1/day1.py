# Advent of Code
# 2019 Day 1 Part 1

from aocCommon import commonFunctions
from pathlib import Path

def calculateFuel(mass):
    return ((mass // 3) -2)

def calculateFuelByFuel(fuel):
    if ((fuel // 3) - 2) <= 0:
        return fuel
    else:
        return fuel + calculateFuelByFuel((fuel // 3) - 2)

def calculateFuelByMass(mass):
    return calculateFuelByFuel(mass) - mass

def main(arg):
    fuel1 = 0
    fuel2 = 0

    for line in commonFunctions.getInput(arg):

        # Part 1
        fuel1 += calculateFuel(commonFunctions.parseInt(line))

        # Part 2
        fuel2 += calculateFuelByMass(commonFunctions.parseInt(line))
    
    print("Part 1: {0} \nPart 2: {1}".format(fuel1, fuel2))
