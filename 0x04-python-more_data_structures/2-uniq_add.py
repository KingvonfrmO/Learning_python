def uniq_add(my_list=[]):
	unique_elements = []
	total = 0
	for i in my_list:
		if i not in unique_elements:
			unique_elements.append(i)

	for i in unique_elements:
		total += i

	return total