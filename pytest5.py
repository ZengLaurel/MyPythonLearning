# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
num = []
for i in range(0, 3):
    x = int(input())
    num.append(x)
num.sort()
print(num)
