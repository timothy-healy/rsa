def fast_power(x, y, n):
    a = x
    b = 1

    while y > 0:
        if y % 2 == 1:
            b = (b*a) % n
        a = (a**2) % n
        y = y //2

    return b
