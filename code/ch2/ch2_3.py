# ch2_3.py
import matplotlib.pyplot as plt
x = [x for x in range(1, 101)]    # 相当于数列 n           
y = [1 / y for y in x]    
plt.axis([0, 100, 0, 2])
plt.plot(x, y)
plt.xlabel("n")
plt.ylabel("y")
plt.grid()                              
plt.show()  
          



