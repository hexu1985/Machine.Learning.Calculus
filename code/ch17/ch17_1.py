# ch17_1.py
import numpy as np

X = np.array([[1, 1], [1, 2], [1, 3]])
XT = X.transpose()
XTX = XT @ X
XTX_inv = np.linalg.inv(XTX)
y = np.array([[5], [10], [20]])
B = XTX_inv @ XT @ y

print(f'a = {B[1][0]}')
print(f'b = {B[0][0]}')


















