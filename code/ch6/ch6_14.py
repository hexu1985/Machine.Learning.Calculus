# ch6_14.py
import matplotlib.pyplot as plt
import numpy as np

n = 10
x = np.linspace(0, 1, n+1)
area = 0
for i in range(n):
    f = x[i] ** 2
    area += f
s = area / n
print(f'较小面积 = {s:6.3f}')

area = 0
for i in range(1, n+1):
    f = x[i] ** 2
    area += f
l = area / n
print(f'较大面积 = {l:6.3f}')
average = (s + l) / 2
print(f'平均面积 = {average:6.3f}')















