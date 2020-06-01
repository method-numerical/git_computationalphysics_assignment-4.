import numpy as np
import matplotlib.pyplot as plt 

x1=np.random.rand(10000)
x2=np.random.rand(10000)
y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)

plt.hist(y1,bins=20,density=True) 

xdata=np.linspace(min(y1),max(y1)) 
ydata=np.exp(-xdata**2/2)/np.sqrt(2*np.pi) 

plt.plot(xdata,ydata,label='gaussian pdf.')

plt.xlabel('random number..')
plt.ylabel('density.')
plt.title('box muller method: gaussian pdf.')

plt.legend()
plt.show() 