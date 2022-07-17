# 斐波那契数列。0 1 1 2 3 5
i = 0
j = 1
k = 0
print("0")
print(1)
for cnt in range(2, 10):
    k = i + j
    print(k)
    i = j
    j = k
