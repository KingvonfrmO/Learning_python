import sys

argv = sys.argv[1:]  # Get arguments excluding the script name
num_argv = len(argv)  # Count the number of arguments

if num_argv == 0:
    print("{} arguments.".format(num_argv))
elif num_argv == 1:
    print("{} argument:".format(num_argv))
    print("1: {}".format(argv[0]))
else:
    print("{} arguments:".format(num_argv))
    for i in range(num_argv):
        print("{}: {}".format(i + 1, argv[i]))
