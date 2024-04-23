def uniq_add(my_list=[]):
    new_list = []
    for items in my_list:
        if items not in new_list:
            new_list.append(items)

    total = 0
    for uniq in new_list:
        total += uniq

    return total
