# ch21_11.py
import numpy as np

def f1():
    ''' 1 - 54 '''
    x1 = beta[0] + delta_x + np.log(1 + np.exp(-(beta[0] + delta_x)))
    x2 = beta[0] + np.log(1 + np.exp(-beta[0]))
    beta0 = people[0] * (x1 - x2) / delta_x
    cur_beta[0] += beta0

def f2():
    ''' 55 - 90 '''
    x1 = np.log(1 + np.exp(-(beta[0] + delta_x)))
    x2 = np.log(1 + np.exp(-beta[0]))
    beta0 = people[1] * (x1 - x2) / delta_x
    cur_beta[0] += beta0

def f3():
    ''' 91 - 108 '''
    x1 = beta[0] + delta_x + beta[2] \
         + np.log(1+np.exp(-(beta[0] + delta_x + beta[2])))
    x2 = beta[0] + beta[2] + np.log(1 + np.exp(-(beta[0] + beta[2])))
    beta0 = people[2] * (x1 - x2) / delta_x
    cur_beta[0] += beta0
    beta2 = beta0
    cur_beta[2] += beta2

def f4():
    ''' 109 - 120 '''
    x1 = np.log(1+np.exp(-(beta[0] + delta_x + beta[2])))
    x2 = np.log(1 + np.exp(-(beta[0]+beta[2])))
    beta0 = people[3] * (x1 - x2) / delta_x
    cur_beta[0] += beta0
    beta2 = beta0
    cur_beta[2] += beta2

def f5():
    ''' 121 - 184 '''
    x1 = beta[0] + delta_x + beta[1] \
         + np.log(1 + np.exp(-(beta[0] + delta_x + beta[1])))
    x2 = beta[0] + beta[1] + np.log(1 + np.exp(-(beta[0] + beta[1])))
    beta0 = people[4] * (x1 - x2) / delta_x
    cur_beta[0] += beta0
    beta1 = beta0
    cur_beta[1] += beta1

def f6():
    ''' 185 - 280 '''
    x1 = np.log(1+np.exp(-(beta[0] + delta_x + beta[1])))
    x2 = np.log(1 + np.exp(-(beta[0] + beta[1])))
    beta0 = people[5] * (x1 - x2) / delta_x
    cur_beta[0] += beta0
    beta1 = beta0
    cur_beta[1] += beta1

def f7():
    ''' 280 - 288 '''
    x1 = beta[0] + delta_x + beta[1] + beta[2] \
         + np.log(1 + np.exp(-(beta[0] + delta_x + beta[1] + beta[2])))
    x2 = beta[0] + beta[1] + beta[2] \
         + np.log(1 + np.exp(-(beta[0] + beta[1] + beta[2])))
    beta0 = people[6] * (x1 - x2) / delta_x
    cur_beta[0] += beta0
    beta1 = beta0
    cur_beta[1] += beta1
    beta2 = beta0
    cur_beta[2] += beta2

def f8():
    ''' 289 - 300 '''
    x1 = np.log(1 + np.exp(-(beta[0] + delta_x + beta[1] + beta[2])))
    x2 = np.log(1 + np.exp(-(beta[0] + beta[1] + beta[2])))
    beta0 = people[7] * (x1 - x2) / delta_x
    cur_beta[0] += beta0
    beta1 = beta0
    cur_beta[1] += beta1
    beta2 = beta0
    cur_beta[2] += beta2

delta_x = 0.00001
rate = 0.003                                        # 学习率
people = [54, 36, 18, 12, 64, 96, 8, 12]            # 各阶段人数
beta = [1, 1, 1]                                    # 初值
for i in range(500):
    cur_beta = [0, 0, 0]
    f1()
    f2()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()
    cur_beta[0] = beta[0] - cur_beta[0] * rate
    cur_beta[1] = beta[1] - cur_beta[1] * rate
    cur_beta[2] = beta[2] - cur_beta[2] * rate
    beta = cur_beta
    #print(beta)                    # 可以打印回归系数的收敛过程
    
print(f'回归系数 {beta[0]:6.5f}, {beta[1]:6.5f}, {beta[2]:6.5f}')



















