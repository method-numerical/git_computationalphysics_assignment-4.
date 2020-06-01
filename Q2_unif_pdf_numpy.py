import numpy as np 
import matplotlib.pyplot as plt 

n=10000

arr=np.random.rand(n)

xdata=np.linspace(0,1)
ydata=np.ones(len(xdata))

plt.hist(arr,bins=20,density=True)
plt.plot(xdata,ydata,label='uniform pdf.')

plt.xlabel('random number..')
plt.ylabel('density.')
plt.title('10000 uniform deviates between 0,1 using numpy.')

plt.legend()
plt.show()