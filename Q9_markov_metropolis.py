import numpy as np 
import matplotlib.pyplot as plt 

n=1000
theta=4

def f(x):
  if 3<=x<=7:
    return 1
  else:
    return 0
    
k=[]
x=[]

for i in range(n):
  theta_prime=theta+np.random.standard_normal() 
  r=np.random.rand()
  if (f(theta)>0)and(f(theta_prime)/f(theta)>r):
    theta = theta_prime
  k.append(theta)
  x.append(i)

plt.figure(figsize=[7,10])

plt.subplot(211)
plt.plot(x,k,label='markov chain.')
plt.xlabel('step proceed.')
plt.ylabel('theta.')
plt.legend()
plt.title('uniform distribution in [3,7].')

plt.subplot(212)
plt.hist(k,density=True)
plt.xlabel('random numbers.')
plt.ylabel('density.')
plt.title('uniform density in [3,7].')

plt.show() 