# ch21_4.py
import numpy as np

x1 = np.log(1 + np.exp(-1.00001))
x2 = np.log(1 + np.exp(-1))
diff = (x1 - x2) / 0.00001
print(f'微分值 = {diff:5.4f}')
beta0 = diff * 36
print(f'beta0  = {beta0:5.4f}')


















