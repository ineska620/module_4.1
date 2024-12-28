def divide(fist, second):
    if second != 0:
        i = fist / second
        print(i)
        return i
    elif second == 0:
        from math import inf
        return inf
