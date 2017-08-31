#!/usr/bin/python3
# -*- coding: utf-8 -*
height = 1.75
weight = 80.5
bmi = weight / (height * height)
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
if bmi < 18.5:
    print('bmi:%.1f,过轻' % bmi)
elif bmi < 25:
    print('bmi:%.1f,正常' % bmi)
elif bmi < 28:
    print('bmi:%.1f,过重' % bmi)
elif bmi < 32:
    print('bmi:%.1f,肥胖' % bmi)
elif bmi >= 32:
    print('bmi:%.1f,严重肥胖' % bmi)

sum = 0
for x in range(101):
    sum += x
print(sum)

ls = ['a', 'b', 'c']
for x in ls:
    print('hello %s' % x)
