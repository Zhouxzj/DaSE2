def find_value_pai_1(num):
    s = 0
    for i in range(num):
        s += (-1) ** i * (1 / (2 * i + 1))
    s = 4 * s
    print("第一种方法的结果为%.8f" % s)
    return


def find_value_pai_2():
    return


find_value_pai_1(1000000)
