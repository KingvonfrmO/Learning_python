for i in range(122, 96, -1):
	if i % 2 == 0:
		print("{:c}".format(i), end="")
	else:
		i = i - 32
		print("{:c}".format(i), end="")

