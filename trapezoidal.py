from sympy import *

def trape_input():
    fun = input('Enter a function in python acceptable format in terms of x, eg instead of x^2 enter X**2, instead of e^x, enter exp(x)!  ')
    trape_input.expression = sympify(fun)
    return(trape_input.expression)

def funct(val):
    x = var('x')
    sum = trape_input.expression.subs(x,val).evalf()
    return(sum)

def trapezoidal():
    trape_input()
    print('Enter range of definite integral! ')
    a,b = float(input('Enter lower value: ')),float(input('Enter upper value: '))
    n = int(input('Enter value for n: '))
    h = (b-a)/n
    s = funct(a)+funct(b)
    for i in range(1,n):
        s = s + (2*funct(a+(i*h)))
    print('Value of function is:\t',end=" ")
    return((h/2)*s)

print(trapezoidal())
