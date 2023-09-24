import math
import random


def find_value_pai_1(num):
    # 级数方法
    s = 0
    i = 0
    pi = math.pi
    while abs(4 * s - pi) > num:
        s += (-1) ** i * (1 / (2 * i + 1))
        i += 1
    s = 4 * s
    print("第一种方法的结果为%.10f,需要迭代%d步" % (s, i))
    return


def find_value_pai_2(precision):
    # 蒙特卡罗随机投点法
    cnt = 10000
    pi = 0
    while abs(pi - math.pi) > precision:
        circle = 0
        out_circle = 0
        i = 0
        while i < cnt:
            i += 1
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if (pow(x, 2) + pow(y, 2)) < 1:
                circle += 1
            else:
                out_circle += 1
        cnt += 1
        pi = 4 * (circle / 1.0) / (out_circle + circle)
    print("第二种方法的结果为%.10f,需要迭代%d步" % (pi, cnt))
    return


def length(x):
    h = math.sqrt(1 - (x / 2) ** 2)
    return math.sqrt((x / 2) ** 2 + (1 - h) ** 2)


def find_value_pai_3(precision):
    # 祖冲之割圆法
    side_length = 1  # 初始边长
    edges = 6  # 初始边数
    cnt = 0
    pi = 0
    while abs(pi - math.pi) > precision:
        for i in range(cnt):
            side_length = length(side_length)
            edges *= 2
            pi = side_length * edges / 2
        cnt += 1
    print("第三种方法的结果为%.15f,需要迭代%d步" % (pi, cnt))
    return


def sumk(k):
    s = 1
    for i in range(1, k + 1):
        s *= i
    return s


def find_value_pai_4(precision):
    # 拉马努金公式算法
    cnt = 1
    pi = 0
    while abs(pi - math.pi) > precision:
        a = 0
        for i in range(cnt):
            a += (sumk(4 * i)) * (1103 + 26390 * i) / (sumk(i) ** 4 * 396 ** (4 * i))
        pi = 1 / a * 9801 / 2 / 2 ** (1 / 2)
        cnt += 1
    print("第四种方法的结果为%.15f,需要迭代%d步" % (pi, cnt))
    return pi


find_value_pai_1(0.00001)
find_value_pai_2(0.00001)
find_value_pai_3(0.00000000001)
find_value_pai_4(0.00000000001)
