import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
import numpy.polynomial.polynomial as pol

f2=lambda x:1/(1+x**2)
x=np.linspace(3,8,10)
y=f2(x)
plt.plot(x,y)


def pol_lagrange(f,rangeStart,rangeEnd,nbr):
    x=np.array([rangeStart,rangeEnd,nbr])
    y=f(x)
    poly= lagrange(x,y)
    pol.Polynomial([rangeStart,rangeEnd,nbr])
    
    plt.plot(x,poly)
    plt.show()
 

pol_lagrange(f2,-5,5,10)




"""def pol_lag(f,a,b,n):
    x=np.linspace(a,b,n)
    X=np.poly1d([1.0])
    y=f(x)
    l=1
    while i,j in range[:n+1]:
        i=j+1
        l=sum(y[j] * (np.prod(X-x[i])/(x[j]-x[i]))
    return l
"""


def lagrange(f,rangeStart,rangeEnd,n):
    x = np.linspace(rangeStart,rangeEnd, n + 1)
    X = np.poly1d([1, 0])
    P = 0
    for i in range(n + 1):
        L = 1

        for j in range(0, i):
            L = L * (X - x[j]) / (x[i] - x[j])

        for j in range(i + 1, n + 1):
            L = L * (X - x[j]) / (x[i] - x[j])

        P = P + L * f(x[i])
        plt.plot(x,P)
    return P