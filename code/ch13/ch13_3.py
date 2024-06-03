# ch13_3.py
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

x = np.linspace(-3, 3, 1000)
plt.plot(x, st.norm.pdf(x, loc=0, scale=1))
plt.plot(x, st.norm.pdf(x, loc=-1, scale=2))
plt.plot(x, st.norm.pdf(x, loc=1, scale=0.5))
plt.grid()
plt.show()













