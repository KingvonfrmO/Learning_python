def delete_at(my_list=[], idx=0):
	if idx < 0 or idx > len(my_list):
		return my_list

	my_list.remove(my_list[idx])
	return my_list