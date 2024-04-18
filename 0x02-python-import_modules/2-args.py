import sys

Number_of_arguments = len(sys.argv) - 1

if Number_of_arguments == 0:
    print("0 arguments.",end = "")
elif Number_of_arguments == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(Number_of_arguments))

for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
    