# Advent of Code
# 2019 Day 2 Parts 1 & 2

from aocCommon import commonFunctions

def process(a_list):
	og = a_list.copy()
	length = len(og) - 1

	for i in range(0, length, 4):
		if a_list[i] == 1:
			opCode1(a_list, i)
		elif a_list[i] == 2:
			opCode2(a_list, i)
		elif i == 17:
			break

	return a_list


def opCode1(a_list, index):
		a_list[a_list[index + 3]] = a_list[a_list[index + 1]] + a_list[a_list[index + 2]]

def opCode2(a_list, index):
		a_list[a_list[index + 3]] = a_list[a_list[index + 1]] * a_list[a_list[index + 2]]

def part1(a_list):

	a_list[1] = 12
	a_list[2] = 2
	process(a_list)

	print("Part 1:", a_list[0])

def resetList(og_list):
	return og_list.copy()

def part2(a_list):

	og_copy = a_list.copy()

	for noun in range(99):
		for verb in range(99):
			a_list[1] = noun
			a_list[2] = verb
			process(a_list)
			if a_list[0] == 19690720:
				return (noun, verb)
			else:
				a_list = resetList(og_copy)

	return None


def main(arg):

	the_list = commonFunctions.getInputListInts(arg)
	the_list2 = the_list.copy()
	part1(the_list)
	print("Part 2: ", part2(the_list2))
	