def multiply_by_2(a_dictionary):
	new_dictionary = {}
	for k , v in a_dictionary.items():
		new_dictionary.update({k: v * 2})
	return new_dictionary