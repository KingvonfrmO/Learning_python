from calculator_1 import add, sub, mul, div
import sys

argv = sys.argv[1:]
arg_count = len(argv)

operators = ["+","-","*","/"]

if arg_count != 3:
	print("Usage: ./100-my_calculator.py <a> <operator> <b>")
	sys.exit(1)

if argv[1] not in operators:
	print("Unknown operator. Available operators: +, -, * and /")
	sys.exit(1)

if argv[1] == "+":
	print(add(int(argv[0]), int(argv[2])))
elif argv[1] == "-":
	print(sub(int(argv[0]), int(argv[2])))
elif argv[1] == "*":
	print(mul(int(argv[0]), int(argv[2])))
elif argv[1] == "/":
	print(div(int(argv[0]), int(argv[2])))
