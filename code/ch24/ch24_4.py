# ch24_4.py
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
print(f"Error_total  = : {Error_total:5.4f}")
#计算新的 w5 权重
dError_total_dy1_out = - (goal[1] - y1_out)
print(f"dError_total_dy1_out  = : {dError_total_dy1_out:5.4f}")
dy1_out_dy1_in = y1_out*(1 - y1_out)
print(f"dy1_out_dy1_in        = : {dy1_out_dy1_in:5.4f}")
dy1_in_dw5 = u1_out
print(f"dy1_in_dw5            = : {dy1_in_dw5:5.4f}")
dError_total_dw5 = dError_total_dy1_out * dy1_out_dy1_in * dy1_in_dw5
print(f"dError_total_dw5      = : {dError_total_dw5:5.4f}")
new_w[5] = w[5] - rate * dError_total_dw5
print(f"  ------------------ new_w5  = : {new_w[5]:8.7f}")
#计算新的 w6 权重
dError_total_dy1_out = - (goal[1] - y1_out)
print(f"dError_total_dy1_out  = : {dError_total_dy1_out:5.4f}")
dy1_out_dy1_in = y1_out*(1 - y1_out)
print(f"dy1_out_dy1_in        = : {dy1_out_dy1_in:5.4f}")
dy1_in_dw6 = u2_out
print(f"dy1_in_dw5            = : {dy1_in_dw5:5.4f}")
dError_total_dw6 = dError_total_dy1_out * dy1_out_dy1_in * dy1_in_dw6
print(f"dError_total_dw6      = : {dError_total_dw6:5.4f}")
new_w[6] = w[6] - rate * dError_total_dw6
print(f"  ------------------ new_w6  = : {new_w[6]:8.7f}")
#计算新的 w7 权重
dError_total_dy2_out = - (goal[2] - y2_out)
print(f"dError_total_dy2_out  = : {dError_total_dy2_out:5.4f}")
dy2_out_dy2_in = y2_out*(1 - y2_out)
print(f"dy1_out_dy2_in        = : {dy2_out_dy2_in:5.4f}")
dy2_in_dw7 = u1_out
print(f"dy2_in_dw7            = : {dy2_in_dw7:5.4f}")
dError_total_dw7 = dError_total_dy2_out * dy2_out_dy2_in * dy2_in_dw7
print(f"dError_total_dw7      = : {dError_total_dw7:5.4f}")
new_w[7] = w[7] - rate * dError_total_dw7
print(f"  ------------------ new_w7  = : {new_w[7]:8.7f}")
#计算新的 w8 权重
dError_total_dy2_out = - (goal[2] - y2_out)
print(f"dError_total_dy2_out  = : {dError_total_dy2_out:5.4f}")
dy1_out_dy2_in = y2_out*(1 - y2_out)
print(f"dy1_out_dy2_in        = : {dy1_out_dy2_in:5.4f}")
dy1_in_dw8 = u2_out
print(f"dy1_in_dw8            = : {dy1_in_dw8:5.4f}")
dError_total_dw8 = dError_total_dy2_out * dy1_out_dy2_in * dy1_in_dw8
print(f"dError_total_dw8      = : {dError_total_dw8:5.4f}")
new_w[8] = w[8] - rate * dError_total_dw8
print(f"  ------------------ new_w8  = : {new_w[8]:8.7f}")
#计算新的 w1 权重
dError1_dy1_out = dError_total_dy1_out
dError1_dout_y1_in = dError1_dy1_out * dy1_out_dy1_in
print(f"dError1_dout_y1_in    = : {dError1_dout_y1_in:5.4f}")
dy1_in_du1_out = w[5]
dError1_du1_out = dError1_dout_y1_in * dy1_in_du1_out
print(f"dError1_du1_out       = : {dError1_du1_out:5.4f}")
dError2_dy2_out = dError_total_dy2_out
dError2_dout_y2_in = dError2_dy2_out * dy2_out_dy2_in
print(f"dError2_dout_y2_in    = : {dError2_dout_y2_in:5.4f}")
dy2_in_du1_out = w[7]
dError2_du1_out = dError2_dout_y2_in * dy2_in_du1_out
print(f"dError2_du2_out       = : {dError2_du1_out:5.4f}")
dError_total_du1_out = dError1_du1_out + dError2_du1_out
print(f"dError_total_du1_out  = : {dError_total_du1_out:5.4f}")
du1_out_du1_in = u1_out * (1 - u1_out)
print(f"du1_out_du1_in        = : {du1_out_du1_in:5.4f}")
du1_in_dw1 = x[1]
print(f"du1_in_dw1            = : {du1_in_dw1:5.4f}")
dError_total_dw1 = dError_total_du1_out * du1_out_du1_in * du1_in_dw1
print(f"dError_total_dw1      = : {dError_total_dw1:5.4f}")
new_w[1] = w[1] - rate * dError_total_dw1
print(f"  ------------------ new_w1  = : {new_w[1]:8.7f}")
#计算新的 w2 权重
dError1_dy1_out = dError_total_dy1_out
dError1_dout_y1_in = dError1_dy1_out * dy1_out_dy1_in
print(f"dError1_dout_y1_in    = : {dError1_dout_y1_in:5.4f}")
dy1_in_du1_out = w[5]
dError1_du1_out = dError1_dout_y1_in * dy1_in_du1_out
print(f"dError1_du1_out       = : {dError1_du1_out:5.4f}")
dError2_dy2_out = dError_total_dy2_out
dError2_dout_y2_in = dError2_dy2_out * dy2_out_dy2_in
print(f"dError2_dout_y2_in    = : {dError2_dout_y2_in:5.4f}")
dy2_in_du1_out = w[7]
dError2_du1_out = dError2_dout_y2_in * dy2_in_du1_out
print(f"dError2_du2_out       = : {dError2_du1_out:5.4f}")
dError_total_du1_out = dError1_du1_out + dError2_du1_out
print(f"dError_total_du1_out  = : {dError_total_du1_out:5.4f}")
du1_out_du1_in = u1_out * (1 - u1_out)
print(f"du1_out_du1_in        = : {du1_out_du1_in:5.4f}")
du1_in_dw2 = x[2]
print(f"du1_in_dw1            = : {du1_in_dw1:5.4f}")
dError_total_dw2 = dError_total_du1_out * du1_out_du1_in * du1_in_dw2
print(f"dError_total_dw1      = : {dError_total_dw2:5.4f}")
new_w[2] = w[2] - rate * dError_total_dw2
print(f"  ------------------ new_w2  = : {new_w[2]:8.7f}")    
#计算新的 w3 权重    
dError1_dy1_out = dError_total_dy1_out
dError1_dout_y1_in = dError1_dy1_out * dy1_out_dy1_in
print(f"dError1_dout_y1_in    = : {dError1_dout_y1_in:5.4f}")
dy1_in_du2_out = w[6]
dError1_du2_out = dError1_dout_y1_in * dy1_in_du2_out
print(f"dError1_du2_out       = : {dError1_du2_out:5.4f}")
dError2_dy2_out = dError_total_dy2_out
dError2_dout_y2_in = dError2_dy2_out * dy2_out_dy2_in
print(f"dError2_dout_y2_in    = : {dError2_dout_y2_in:5.4f}")
dy2_in_du2_out = w[8]
dError2_du2_out = dError2_dout_y2_in * dy2_in_du2_out
print(f"dError2_du2_out       = : {dError2_du2_out:5.4f}")
dError_total_du2_out = dError1_du2_out + dError2_du2_out
print(f"dError_total_du2_out  = : {dError_total_du2_out:5.4f}")
du2_out_du2_in = u2_out * (1 - u2_out)
print(f"du2_out_du2_in        = : {du2_out_du2_in:5.4f}")
du2_in_dw3 = x[1]
print(f"du2_in_dw3            = : {du2_in_dw3:5.4f}")
dError_total_dw3 = dError_total_du2_out * du2_out_du2_in * du2_in_dw3
print(f"dError_total_dw3      = : {dError_total_dw3:5.4f}")
new_w[3] = w[3] - rate * dError_total_dw3
print(f"  ------------------ new_w3  = : {new_w[3]:8.7f}")
#计算新的 w4 权重    
dError1_dy1_out = dError_total_dy1_out
dError1_dout_y1_in = dError1_dy1_out * dy1_out_dy1_in
print(f"dError1_dout_y1_in    = : {dError1_dout_y1_in:5.4f}")
dy1_in_du2_out = w[6]
dError1_du2_out = dError1_dout_y1_in * dy1_in_du2_out
print(f"dError1_du2_out       = : {dError1_du2_out:5.4f}")
dError2_dy2_out = dError_total_dy2_out
dError2_dout_y2_in = dError2_dy2_out * dy2_out_dy2_in
print(f"dError2_dout_y2_in    = : {dError2_dout_y2_in:5.4f}")
dy2_in_du2_out = w[8]
dError2_du2_out = dError2_dout_y2_in * dy2_in_du2_out
print(f"dError2_du2_out       = : {dError2_du2_out:5.4f}")
dError_total_du2_out = dError1_du2_out + dError2_du2_out
print(f"dError_total_du2_out  = : {dError_total_du2_out:5.4f}")
du2_out_du2_in = u2_out * (1 - u2_out)
print(f"du2_out_du2_in        = : {du2_out_du2_in:5.4f}")
du2_in_dw4 = x[2]
print(f"du2_in_dw4            = : {du2_in_dw4:5.4f}")
dError_total_dw4 = dError_total_du2_out * du2_out_du2_in * du2_in_dw4
print(f"dError_total_dw4      = : {dError_total_dw4:5.4f}")
new_w[4] = w[4] - rate * dError_total_dw4
print(f"  ------------------ new_w4  = : {new_w[4]:8.7f}")


















