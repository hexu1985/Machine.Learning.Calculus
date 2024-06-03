# ch19_1.py
import matplotlib.pyplot as plt
import numpy as np
import time

rate = eval(input("请输入学习率 : "))
init_x = eval(input("请输入参数值 : "))

x = np.arange(-10, 10, 0.1)
y = x**2
plt.plot(x, y)                             # 绘制函数

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
    new_x = old_x - rate * 2 * old_x        # 计算新的参数
    
    plt.plot([old_x, new_x], [old_x**2, new_x**2], 'go-')
    print(f'loop = {i:2d},  old_x = {old_x:4.2f},  new_x = {new_x:4.2f}')
    time.sleep(1)

plt.grid()
plt.show()



        
    

    



















