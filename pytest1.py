# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
i = 1
j = 1
k = 1
while i <= 4:
    while j <= 4:
        while k <= 4:
            if i != j and i != k and j != k:
                a = i * 100 + j * 10 + k
                print(a)
            k = k + 1
        j = j + 1
        k = 1
    i = i + 1
    j = 1
print("\n")
