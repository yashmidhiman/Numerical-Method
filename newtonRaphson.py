import numpy as np
import math
from sympy import *
import matplotlib.pyplot as plt

X = []
Y = []
def nr_input():
    fun = input('Enter a function!  ')
    nr_input.expression = sympify(fun)
    return(nr_input.expression)

def funct(val):
    x = var('x')
    sum = nr_input.expression.subs(x,val).evalf()
    return(sum)

def derivative(val):
    x = var('x')
    f = diff(nr_input.expression, x)
    sum1 = f.subs(x,val).evalf()
    #print(sum1)
    return(sum1)
    
def newtonRaphson():
    nr_input()
    a = float(input("Enter initial value: "))
    h = funct(a)/derivative(a)
    X.append(a)
    Y.append(h)
    while(h**2 >= 0.0001):
        h = funct(a)/derivative(a)
        a = a-h
        X.append(a)
        Y.append(h)
    return(a)

def plot_Graph():
    #colors = []
    colors = np.arange(10,len(X)+10)
    plt.scatter(X,Y,c = colors,s = 20,cmap = plt.get_cmap('Blues'), marker = 'o')
    plt.show()

print(newtonRaphson())
plot_Graph()
