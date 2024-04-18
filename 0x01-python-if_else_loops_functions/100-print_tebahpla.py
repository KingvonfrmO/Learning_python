for ch in range(122, 96, -1):
    if ch % 2 == 0:
        print(chr(ch),end = "")
    else:
        print(chr(ch - 32), end = "")
    