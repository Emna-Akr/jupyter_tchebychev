import numpy as np
import matplotlib.pyplot as plt 
from utils_lag import *
from math import cos, pi


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
    

f=lambda x:x**45

represent(f,0,3,100)

tchebychev(3,3)
