# 九九乘法表
i = 1
j = 1
for i in range(1, 10):
    print("\n")
    for j in range(1, i + 1):
        print("%d * %d = %d " % (j, i, i * j), end=" ")
