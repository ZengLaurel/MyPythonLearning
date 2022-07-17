# 题目：输入某年某月某日，判断这一天是这一年的第几天？
year = int(input("年份："))
m = int(input("月份："))
day = int(input("日："))
ran = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0
for cnt in range(1, m):
    sum += ran[cnt]
if year % 4 == 0:
    sum += 1
sum += day
print(sum)
