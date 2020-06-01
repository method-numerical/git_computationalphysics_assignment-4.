import numpy as np

n=10000 

#area of circle.
x=2*np.random.rand(n)-1
y=2*np.random.rand(n)-1

k=0 
for p in range(n):
  if x[p]**2+y[p]**2<=1:
    k+=1
A2=2**2*(k/n) 
print('area of unit circle',A2,'.')

#area of 10d sphere.

a=2*np.random.rand(n)-1
b=2*np.random.rand(n)-1
c=2*np.random.rand(n)-1
d=2*np.random.rand(n)-1
e=2*np.random.rand(n)-1
f=2*np.random.rand(n)-1
g=2*np.random.rand(n)-1
h=2*np.random.rand(n)-1
i=2*np.random.rand(n)-1
j=2*np.random.rand(n)-1

l=0 
for q in range(n):
  if a[q]**2+b[q]**2+c[q]**2+d[q]**2+e[q]**2+f[q]**2+g[q]**2+h[q]**2+i[q]**2+j[q]**2<=1:
    l+=1
V=2**10*(l/n) 
print('10d unit sphere volume',V,'.') 