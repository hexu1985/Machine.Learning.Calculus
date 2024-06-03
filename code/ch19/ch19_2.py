# ch19_2.py
import matplotlib.pyplot as plt
import numpy as np
import time

def myfun(t):
    return (7*t**2 - 1120*t + 45850)

rate = eval(input("请输入学习率 : "))
init_x = eval(input("请输入参数值 : "))

x = np.arange(0, 200, 0.1)
y = 7*x**2 - 1120*x + 45850
plt.plot(x, y)                              # 绘制函数

plt.xlabel('x')
plt.ylabel('L')
plt.title(f'rate = {rate}    initial = {init_x}')

new_x = 0
old_x = 0
for i in range(1, 16):                      # 15 圈
    if i == 1:
        old_x = init_x
    else:
        old_x = new_x
    slope = 14 * old_x - 1120               # 斜率
    new_x = old_x - rate * slope            # 计算新的参数
    
    plt.plot([old_x, new_x], [myfun(old_x), myfun(new_x)], 'go-')
    print(f'loop = {i:2d},  old_x = {old_x:5.2f},  new_x = {new_x:5.2f}')
    time.sleep(1)

plt.grid()
plt.show()



        
    

    



















