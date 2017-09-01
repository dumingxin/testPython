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


def my_abs(n):
    if n > 0:
        return n
    else:
        return -n


print(my_abs(-10))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s for s in L1 if isinstance(s, str)]
print(L2)


def triangles():
    L = [1]
    while(True):
        yield L
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
        L.insert(0, 1)
        L.append(1)


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
