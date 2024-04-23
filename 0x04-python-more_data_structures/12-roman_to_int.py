def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return None

    roman_dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    prev = 0
    total = 0

    for char in reversed(roman_string):
        value = roman_dictionary.get(char)
        if value is None:
            return 0

        if value < prev:
            total -= value
        else:
            total += value
        prev = value

    return total


