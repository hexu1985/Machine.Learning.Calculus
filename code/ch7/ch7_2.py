# ch7_2.py
from sympy import *
import math

x = Symbol('x')
f = 2*math.pi*x
area = integrate(f, (x, 2.5, 5))            # 卷筒纸的面积
length = area /0.01                         # 计算卷筒纸长度
print(f'卷筒纸的长度是 : {length:5.3f} 公分')























