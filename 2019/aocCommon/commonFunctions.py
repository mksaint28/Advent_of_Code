# aocCommon
# Common functions for aoc 2019

from pathlib import Path

"""
	Returns the lines of the input file
	as a List of Strings (includes whitespace
	characters).

	input: path [String]
	output: lines [List{String}]
"""
def pathResolver(day):
	base_path = Path(__file__).parent.parent
	file_path = (base_path / day / "input.txt").resolve()
	return file_path

def getInput(day):
	path = pathResolver(day)
	file = open(path, "r")
	lines = file.readlines()
	file.close()
	return lines

def getInputListInts(day):
	path = pathResolver(day)
	file = open(path, "r")
	a_list = [parseInt(x) for x in (file.read().strip("\n").split(","))]
	file.close()
	return a_list

def parseInt(string):
	return int(string.strip("\n"))