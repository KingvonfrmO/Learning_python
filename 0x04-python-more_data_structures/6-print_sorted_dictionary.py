def print_sorted_dictionary(a_dictionary):
	sorted_keys = sorted(a_dictionary)

	for k in sorted_keys:
		print(f"{k}: {a_dictionary[k]}")