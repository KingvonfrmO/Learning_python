def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    score = 0
    weight = 0

    for i, j in my_list:
        score += i * j
        weight += j

    if weight == 0:
        return 0

    return score / weight
