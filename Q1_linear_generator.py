import numpy as np 
import matplotlib.pyplot as plt 

a=189708
m=1001
c=898870
x=1

n=10000
arr=[] 

for i in range(n):
  x=(a*x+c)%m/1000
  arr.append(x)

xdata=np.linspace(0,1)
ydata=np.ones(len(xdata))

plt.hist(arr,bins=20,density=True)
plt.plot(xdata,ydata,label='uniform pdf.')

plt.xlabel('random number..')
plt.ylabel('density.')
plt.title('10000 uniform deviates between 0,1.')

plt.legend()
plt.show()