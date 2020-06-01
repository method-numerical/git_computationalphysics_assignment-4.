import numpy as np
from scipy.stats import chi2 

n=144 
exp_cnt=n*np.array([1,2,3,4,5,6,5,4,3,2,1])/36

y1=[4,10,10,13,20,18,18,11,13,14,13]
y2=[3,7,11,15,19,24,21,17,13,9,5]

def result(p):
  if (p<0.01)or(p>=0.99):
    return "not sufficiently random."
  if (0.01<=p<0.05)or(0.95<=p<0.99):
    return "suspect."
  if (0.05<=p<0.1)or(0.9<=p<0.05):
    return "almost suspect."
  else:
    return "sufficiently random." 
  
v1=sum((y1-exp_cnt)**2/exp_cnt)
v2=sum((y2-exp_cnt)**2/exp_cnt) 

p1=1-chi2.cdf(v1,10)
p2=1-chi2.cdf(v2,10) 

print(result(p1))
print(result(p2)) 