def no_c(my_string):
    new_string = ""
    for ch in my_string:
        if ord(ch) != ord("c") and ord(ch) != ord("C"):
            new_string += ch
    return new_string
