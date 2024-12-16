def multiple_returns(sentence):
	if len(sentence) == 0:
		return 0, None
	else:
		my_tuple = len(sentence), sentence[0]

	return my_tuple