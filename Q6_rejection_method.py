import numpy as np
import matplotlib.pyplot as plt 

x=20*np.random.rand(10000)
y=np.random.rand(10000) 

def f(x):
  return np.exp(-x**2/2)/np.sqrt(np.pi/2) 

xacc=x[y<f(x)];yacc=y[y<f(x)]

plt.hist(xacc,density=True) 

xdata=np.linspace(min(xacc),max(xacc)) 
ydata=np.exp(-xdata**2/2)/np.sqrt(np.pi/2)  

plt.plot(xdata,ydata,label='gaussian pdf.')

plt.xlabel('random number..')
plt.ylabel('density.')
plt.title('rejection method: gaussian pdf.')
plt.legend();plt.show() 