
# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''x + 100 = n ^ 2
x + 100 + 168 = m ^ 2
(m + n)(m - n)= 168
i = m + n
j = m - n
i * j = 168
'''
cnt = 0
nums = 0
for i in range(0, 85):
    for j in range(0, 85):
        if i * j == 168:
            m = (i + j)/2
            n = ((i - j)/2)
            if (i + j) % 2 == 0 and (i - j) % 2 == 0:
                x = n * n - 100
                print(x)
