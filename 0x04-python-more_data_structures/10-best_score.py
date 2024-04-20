def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    my_list = list(a_dictionary.keys())
    score = 0
    top = ""
    for i in my_list:
        if a_dictionary[i] > score:
            score = a_dictionary[i]
            top = i
    return top
