import numpy as np
import math
from sympy import *
import matplotlib.pyplot as plt
"""def funct(x):
    #print(inp)
    sum = 0
    j = inp
    for i in range(0,inp):
        while(j > 0):
            sum = sum+(lst[i]*(x**j))
            break
        j = j-1
    sum = sum+lst[inp]
    return(sum)"""
""""str = input("Enter Polynomial: ")
def f(x):
    return()"""

X = []
Y = []

def bis_input():
    fun = input('Enter a function in python acceptable format in terms of x, eg instead of x^2 enter X**2, instead of e^x, enter exp(x)!  ')
    bis_input.expression = sympify(fun)
    return(bis_input.expression)

def funct(val):
    x = var('x')
    sum = bis_input.expression.subs(x,val).evalf()
    return(sum)
def bisection():
    bis_input()
    a,b = float(input("Enter lower limit of range: ")),float(input("Enter upper limit of range: "))
    if(funct(a)*funct(b) >= 0):
        print('root does not lie here')
    else:
        X.append(a)
        Y.append(b)
        while(b-a)/2 > 0.00001:
            midpoint = (a+b)/2
            if funct(midpoint) == 0.0:
                return(midpoint)
            elif funct(a)*funct(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
            X.append(a)
            Y.append(b)
        return(midpoint)

def plot_Graph():
    #colors = []
    colors = np.arange(10,len(X)+10)
    plt.scatter(X,Y,c = colors,s = 20,cmap = plt.get_cmap('Blues'), marker = 'o')
    plt.show()
    
print(bisection())
plot_Graph()
"""

a,b = int(input("Enter lower limit of range: ")),int(input("Enter upper limit of range: "))
"""
