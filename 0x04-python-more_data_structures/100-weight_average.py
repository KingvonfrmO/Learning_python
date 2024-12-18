def weight_average(my_list=[]):
	if len(my_list) == 0:
		return 0

	multiplication = 0
	division = 0

	for row in my_list:
		multiplication += row[0] * row[1]
		division += row[1]

	return multiplication / division