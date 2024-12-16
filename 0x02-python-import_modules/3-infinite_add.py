import sys

argv = sys.argv[1:]
arg_count = len(argv)

add = 0
for i in range(arg_count):
	add += int(argv[i])

print(add)