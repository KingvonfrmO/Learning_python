from calculator_1 import add, sub, mul, div
import sys 

Number_of_arguments = len(sys.argv) - 1
if Number_of_arguments != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

List_of_operators = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

if sys.argv[2] not in List_of_operators:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
    
a = int(sys.argv[1])
b = int(sys.argv[3])
print("{} {} {} = {}".format(a, sys.argv[2], b, List_of_operators[sys.argv[2]](a, b)))
    
