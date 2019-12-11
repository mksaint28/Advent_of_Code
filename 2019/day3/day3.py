# Advent of Code
# 2019 Day 3 Part 1

from aocCommon import commonFunctions

def parseWire(a_string):
	return a_string.strip('\n').split(',')

def parseSegments(points):
	x, y = 0, 0
	line_list = []

	for point in points:
		if point[0] == 'R':
			x += int(point[1:])
		elif point[0] == 'L':
			x -= int(point[1:])
		elif point[0] == 'U':
			y += int(point[1:])
		elif point[0] == 'D':
			y -= int(point[1:])
		line_list.append((x,y))

	return line_list

"""
Lines are composed of 2 tuples containing the points.
"""
def determinate(point1, point2):
	det = point1[0] * point2[1] - point1[1] * point2[0]

	return det

def calculateIntersections(segment_list1, segment_list2):

	x1 = segment_list1[0][0]
	x2 = segment_list1[1][0]
	x3 = segment_list2[0][0]
	x4 = segment_list2[1][0]

	y1 = segment_list1[0][1]
	y2 = segment_list1[1][1]
	y3 = segment_list2[0][1]
	y4 = segment_list2[1][1]

	det1 = determinate((x1,y1),(x2,y2))
	det2 = determinate((x3,y3),(x4,y4))

	num1 = (det1 * (x3 - x4)) - ((x1 - x2)*det2)
	num2 = (det1 * (y3 - y4)) - ((y1 - y2)*det2)

	denom1 = ((x1 - x2)*(y3 - y4)) - ((y1 - y2)*(x3 - x4))
	denom2 = ((x1 - x2)*(y3 - y4)) - ((y1 - y2)*(x3 - x4))

	if (det1 != 0) and (det2 != 0) and (denom1 != 0) and (denom2 != 0):
		Px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4))/(((x1 - x2)*(y3 - y4)) - ((y1 - y2)*(x3 - x4)))
		Py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4))/(((x1 - x2)*(y3 - y4)) - ((y1 - y2)*(x3 - x4)))

	else:
		Px, Py = 0, 0

	if (Px, Py) != (0, 0):
		return (Px, Py) 

def buildIntersectionList(wire1, wire2):
	intersection_list = []

	wireSegments1 = parseSegments(wire1)
	wireSegments2 = parseSegments(wire2)

	len1 = len(wireSegments1)
	len2 = len(wireSegments2)

	for i in range(0, len1 - 2, 2):
		for j in range(0, len2 - 2, 2):
			intersection_list.append(calculateIntersections((wireSegments1[i], wireSegments1[i+1]), (wireSegments2[j], wireSegments2[j+1])))

	return intersection_list

def main(arg):
	# the_lines = commonFunctions.getInput(arg)
	the_lines = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
	wire1 = parseWire(the_lines[0])
	wire2 = parseWire(the_lines[1])

	intersections = buildIntersectionList(wire1, wire2)

	intersections = list(filter(lambda a: a != None, intersections))

	print(intersections)