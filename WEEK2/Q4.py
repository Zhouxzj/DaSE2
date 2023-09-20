def square_root_2(num):
    i = 0
    g = 0
    precision = 0.0001
    for j in range(num+1):
        if j**2 > num and g > 0:
            g = j - 1
        while abs(g**2 - num) > precision:
            g += float(precision/10)
            i = i + 1
    print("%d:g = %.5f" % (i, g))
    return


square_root_2(2)
