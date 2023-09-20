def square_root_2(num, x):
    g = num / x
    i = 0
    precision = 0.00000000001
    while abs(g ** 2 - num) > precision:
        g = (g + num / g) / 2
        i += 1
    print("%d:g = %.6f" % (i, g))
    return


for i in [2, 20, 100, 200, 500, 1000, 2000]:
    square_root_2(2, i)
# 发现随着i增大，需要迭代更多次来找到足够精度的结果