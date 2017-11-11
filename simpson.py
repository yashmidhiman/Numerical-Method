from sympy import *

def simp_input():
    fun = input('Enter a function in python acceptable format in terms of x, eg instead of x^2 enter X**2, instead of e^x, enter exp(x)!  ')
    simp_input.expression = sympify(fun)
    return(simp_input.expression)

def funct(val):
    x = var('x')
    sum = simp_input.expression.subs(x,val).evalf()
    print(sum)
    return(sum)

def simpson():
    simp_input()
    print('Enter range of definite integral! ')
    a,b = float(input('Enter lower value: ')),float(input('Enter upper value: '))
    n = int(input('Enter a even value for n: '))
    h = (b-a)/n
    print(h)
    s = funct(a)+funct(b)
    for i in range(1,n-1,2):
        s = s + (4*funct(a+(i*h))) + (2*funct(a+((i+1)*h)))
    s = s + (4*funct(a+((n-1)*h)))
    print('Value of function is:\t',end=" ")
    return((h/3)*s)

print(simpson())
