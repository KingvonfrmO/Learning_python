def complex_delete(a_dictionary, value):
	list_keys = list(a_dictionary.keys())

	for k in list_keys:
		if value == a_dictionary.get(k):
			del a_dictionary[k]

	return a_dictionary