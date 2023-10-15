import random

w = [1, 2, 3]  # 西岸初始状态 0代表没有 1代表菜 2代表羊 3代表狼
e = [0] * 3  # 东岸初始状态
taken = []  # 储存每一步所带的东西
cnt = 0  # 记录人所在位置，单数代表西岸，双数代表东岸

while True:
    if cnt % 2 == 1 and (3 in w and 2 in w or 2 in w and 1 in w) \
            or cnt % 2 == 0 and (3 in e and 2 in e or 2 in e and 1 in e):
        # 如果出现狼羊或羊菜同岸，则刷新状态，出现开始步骤
        w = [1, 2, 3]
        e = [0] * 3
        li = []
        cnt = 0
        continue
    m = random.randint(-1, 2)
    # 随机选择携带状态，-1是不带，0对应菜，1对应羊，2对应狼
    taken.append(m)
    if m != -1 and w[m] != 0 and cnt % 2 == 0:
        # 判断选择的状态物品是否与农夫同岸，同则带过河
        w[m], e[m] = e[m], w[m]  # 带过河即交换两岸对应物品列表元素
    elif m != -1 and e[m] != 0 and cnt % 2 == 1:
        w[m], e[m] = e[m], w[m]
    else:
        taken[-1] = -1
        # 表示在taken列表尾部加上不带东西过河的状态
    if e == [1, 2, 3]:
        break
    cnt += 1

lit = ['不带任何', '菜', '羊', '狼']
for i in range(len(taken) - 1):  # 去除无效步骤，因为可能会出现前一步和后一步完全一样的情况，需要去合并
    if taken[i] == taken[i + 1]:
        taken[i] = taken[i + 1] = []
while [] in taken:
    taken.remove([])
l = len(taken)
for i in taken[l-7:-1]:  # 打印最终步骤
    print(lit[i + 1], end='\t')
print("羊")

