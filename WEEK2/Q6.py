def square_root(num):
    for g in [num, 3 * num / 2, num / 2, num / 4, num / 8]:
        i = 0
        precision = 0.00000000001
        while abs(g ** 2 - num) > precision:
            g = (g + num / g) / 2
            i += 1
        print("%d:g = %.6f" % (i, g))
    return


square_root(2)
# 当g从num/2往大和小逐渐偏移时，所需的迭代次数会逐渐上升
