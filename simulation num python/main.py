    # MAIN PROGRAM:INTERPOLATION LAGRANGIENNE


from utils_lag_tche import *
from math import cos , pi  

"""
Exercices TP_SIMUTATION 
REMOVE the '#'to test each result at a time 
"""

f1=lambda x:1/(1+x)
f2=lambda x:1/(1+x**2)
f3=lambda x:(x+5)/(x+2) 
f4=lambda x:(x-1)**(1/2)

represent(f1,0,5,100)
#represent(f2,-5,5,100)
#represent(f3,3,8,100)
#represent(f4,1,5,100)

lagrange_math(f1,0,5,10)
#lagrange_math(f2,-5,5,3)
#lagrange_math(f3,3,8,10) 
#lagrange_math(f4,1,5,3)





