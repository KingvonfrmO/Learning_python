def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, values in a_dictionary.items():
        new_dictionary[key] = values * 2
    return new_dictionary
