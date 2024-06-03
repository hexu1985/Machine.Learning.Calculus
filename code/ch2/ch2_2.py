# ch2_2.py
import matplotlib.pyplot as plt
alchol = 58
x = [x for x in range(0, 11)]           # 调淡酒精的次数     
y = [alchol * (1/2) ** y for y in x]    # 酒精浓度
plt.axis([0, 12, 0, 60])
plt.plot(x, y)
plt.xlabel("Times")
plt.ylabel("Alcohol concentration")
plt.grid()                              
plt.show()
            



