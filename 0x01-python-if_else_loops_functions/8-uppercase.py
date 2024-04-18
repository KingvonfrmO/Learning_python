def uppercase(str):
    result=""
    for ch in str:
        if ord(ch) >= ord("a") and ord(ch) <= ord("z"):
            result += chr(ord(ch) - 32)
        else:
            result += chr(ord(ch))
    print(result)