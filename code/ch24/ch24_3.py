# ch24_3.py
import numpy as np

rate = 0.1                                      # 学习率
w = [0,0.1,0.15,0.2,0.25,0.4,0.45,0.3,0.2]      # weight, 索引 0 没有作用
new_w = [0, 0, 0, 0, 0, 0, 0, 0, 0]             # new weight, 索引 0 没有作用
x = [0, 0.1, 0.2]                               # x, 索引 0 没有作用
goal = [0, 0.1, 0.9]                            # 目标输出
b = [0, 0.3, 0.7]                               # 偏置值

#计算 u1 神经元的输入
u1_in = w[1]*x[1] + w[2]*x[2] + b[1]
print(f"u1_in        = : {u1_in:5.4f}")
#计算 u1 神经元的输出
u1_out = 1 / (1 + np.exp(-u1_in))               # Sigmoid函数的转换
print(f"u1_out       = : {u1_out:5.4f}")
#计算 u2 神经元的输入
u2_in = w[3]*x[1] + w[4]*x[2] + b[1]
print(f"u2_in        = : {u2_in:5.4f}")
#计算 u2 神经元的输出
u2_out = 1 / (1 + np.exp(-u2_in))               # Sigmoid函数的转换
print(f"u2_out       = : {u2_out:5.4f}")
#计算 y1 输出层的输入
y1_in = w[5]*u1_out + w[6]*u2_out + b[2]
print(f"y1_in        = : {y1_in:5.4f}")
#计算 y1 输出层的输出
y1_out = 1 / (1 + np.exp(-y1_in))               # Sigmoid函数的转换
print(f"y1_out       = : {y1_out:5.4f}")
#计算 y2 输出层的输入
y2_in = w[7]*u1_out + w[8]*u2_out + b[2]
print(f"y2_in        = : {y2_in:5.4f}")
#计算 y2 输出层的输出
y2_out = 1 / (1 + np.exp(-y2_in))               # Sigmoid函数的转换
print(f"y2_out       = : {y2_out:5.4f}")
#计算神经网络整体误差
Error1 = 0.5 * (goal[1] - y1_out)**2            #计算神经网络 y1 的误差
Error2 = 0.5 * (goal[2] - y2_out)**2            #计算神经网络 y2 的误差
Error_total = Error1 + Error2
print(f"Error_total  = : {Error_total:8.7f}")
















