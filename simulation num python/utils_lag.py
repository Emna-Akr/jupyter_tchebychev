    # INTERPOLATION DE LAGRANGE & POLYNOME DE CHEBYSHEV  

import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import lagrange
import numpy.polynomial.polynomial as pol

# A FUNCTION THAT REPRESENT ANY GIVEN MATHMATICAL FUNTION
def represent(f,rangeStart,rangeEnd,nbr):
    #nbr>=0
    #plotting main function
    x=np.linspace(rangeStart,rangeEnd,nbr)
    y=f(x)
    plt.plot(x,y)
    plt.show
    
# CALCULATES AND REPRESENT LAGRANGE POLYNOME USING SCIPY LYBRARY  
def pol_lagrange(f,rangeStart,rangeEnd,nbr):
    x=np.array([rangeStart,rangeEnd,nbr])
    y=f(x)
    poly= lagrange(x,y)
    pol.Polynomial([rangeStart,rangeStart,nbr])
    plt.plot(x,poly)
    plt.title('Lagrange Polynomial')
    return poly

# MATHMATICAL CALCULATION OF LAGRANGE INTERPOLATION PLUS REPRESENTATION 
def lagrange_math(f,rangeStart,rangeEnd,n):
    x = np.linspace(rangeStart,rangeEnd, n + 1)
    X = np.poly1d([1/2, 0])
    P = 0
    for i in range(n + 1):
        L=1
        for j in range(0, i):
            L = L * (X - x[j]) / (x[i] - x[j])

        for j in range(i + 1, n + 1):
            L = L * (X - x[j]) / (x[i] - x[j])
        P = P + L * f(x[i])
    
    plt.plot(x,P)
    a=np.linspace(rangeStart,rangeEnd,n)
    y=f(a)
    plt.plot(a,y)
    return P

# CHEBYSHEV 

def tchebychev(n,x):
    if n == 0:
        pol_tche = (x)**0
        return print('polynome tchebychev',pol_tche)
    elif n == 1:
        pol_tche=x
        return print('polynome tchebychev',pol_tche)
    else:
        pol_tche=2*x*tchebychev(n-1,x)-tchebychev(n-2,x)
        return print('polynome tchebychev',pol_tche)
    