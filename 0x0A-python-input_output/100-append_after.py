def append_after(filename="", search_string="", new_string=""):
	with open(filename) as f:
		text = ""
		for line in f:
			text += line
			if search_string in line:
				text += new_string

	with open(filename, "w") as f:
		f.write(text)