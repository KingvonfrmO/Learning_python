def pascal_triangle(n):
	if n <= 0:
		return []

	new_list = [[1]]
	while len(new_list) != n:
		x = new_list[-1]
		tmp = [1]
		for i in range(len(x) - 1):
			tmp.append(x[i] + x[i + 1])
		tmp.append(1)
		new_list.append(tmp)

	return new_list
