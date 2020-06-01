#connect to internet because the following code import some data from a specified link.

#corner and emcee library should be properly installed and located so that compiler can import them.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

data="http://theory.tifr.res.in/~kulkarni/data.txt"

x=np.loadtxt(data,usecols=1,delimiter='&')
y=np.loadtxt(data,usecols=2,delimiter='&')
sigma_y=np.loadtxt(data,usecols=3,delimiter='&')

def log_likelihood(theta,x,y,yerr):
    a,b,c=theta
    model=a*x**2+b*x+c
    sigma2=sigma_y**2
    return np.sum((y-model)**2/sigma2+np.log(2*np.pi*sigma2))/2

def log_prior(theta):
    a,b,c=theta
    if -4000<a<4000 and -4000<b<4000 and -4000<c<4000:
        return 0
    return -np.inf

def log_probability(theta,x,y,sigma_y):
    lp=log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp-log_likelihood(theta,x,y,sigma_y)

guess=(1,1,1)
soln=minimize(log_likelihood,guess,args=(x,y,sigma_y))

nwalkers,ndim=50,3
pos=soln.x+1e-4*np.random.randn(nwalkers, ndim)

import emcee
sampler=emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x,y,sigma_y))
sampler.run_mcmc(pos,4000)

samples=sampler.get_chain()

plt.figure(figsize=[7,20])

plt.subplot(711)
plt.plot(samples[:,:,0])
plt.xlabel('step number.')
plt.ylabel('a.')

plt.subplot(713)
plt.plot(samples[:,:,1])
plt.xlabel('step number.')
plt.ylabel('b.')

plt.subplot(715)
plt.plot(samples[:,:,2])
plt.xlabel('step number.')
plt.ylabel('c.')

import corner

samples=np.vstack(samples)
median=np.median(samples,axis=0)
a_true,b_true,c_true=median
print('best fit a, b, c are', median,'.')

w_a=corner.quantile(samples[:,0],[0.16,0.84])
w_b=corner.quantile(samples[:,1],[0.16,0.84])
w_c=corner.quantile(samples[:,2],[0.16,0.84])
print('1-sigma uncertainity in a,b,c are',w_a-a_true,w_b-b_true,w_c-c_true,'respectively.')

plt.subplot(717)

x_new=np.linspace(min(x),max(x))
for i in range(200):
    a_model,b_model,c_model=samples[i]
    plt.plot(x_new,a_model*x_new**2+b_model*x_new+c_model,'y')

plt.plot(x_new,a_true*x_new**2+b_true*x_new+c_true,'g',label='best-fit.')
plt.errorbar(x,y,yerr=sigma_y,fmt='.b')

plt.xlabel('x_data.')
plt.ylabel('y_data.')
plt.legend()

fig=corner.corner(samples,labels=['a','b','c'],quantiles=[0.16,0.84],show_titles=True,truths=[a_true,b_true,c_true])

plt.show()

































