import time as t 
import numpy as np 
import matplotlib.pyplot as plt 

n=10000

t1=t.perf_counter()
arr=np.random.rand(n)
t2=t.perf_counter()
print('time for numpy code',t2-t1,'s.')

a=899;m=1001;c=199
x=1

arr=[]

t3=t.perf_counter()
for i in range(n):
  x=(a*x+c)%m
  arr.append(x)
t4=t.perf_counter()
print('time for linear generator',t4-t3,'s.')