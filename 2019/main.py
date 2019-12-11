from day1 import day1
from day2 import day2
from day3 import day3
import sys

def getArg():
	return sys.argv[1]

def run(arg):
	options = {"day1" : day1.main,
			   "day2" : day2.main,
			   "day3" : day3.main
	}

	options[arg](arg)

def main():
	run(getArg())

main()