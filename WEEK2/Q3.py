# 设狼为1，羊为2，菜为3，原岸为0，新岸为1
A = [["狼", 0], ["羊", 0], ["菜", 0]]
count = 0
route = []


def judgement(x):
    if x[0][1] + x[2][1] == 1:
        return False
    else:
        return True


def pass_river(x, cnt, way):
    if x[0][1] * x[1][1] * x[2][1] == 1:
        return
    for j in range(3):
        x[j][1] = 1 - x[j][1]
        if judgement(x):
            way.append(x[j][1])
            cnt += 1
            pass_river(x, cnt, way)
        else:
            x[j][1] = 1 - x[j][1]


pass_river(A, count, route)
for i in range(count):
    print(route[i] + "过河了")
print("一共用了%d步" % count)