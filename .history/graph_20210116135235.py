from sympy import *
import pandas as pd

x=Symbol("x")
a=0
list=[]
for i in range(10):
    a=a+diff(x**2,x).subs('x',i).evalf(n=3)
    list.append(float(a))
s = pd.Series(list)
s.plot()
