'''Interpolation'''
from matplotlib.pylab import *
from math import sin
def dif(i1,i2):
    return (y[i2]-y[i1])/(x[i2]-x[i1])
def f(x):
    return sin(x)
def inte(a):
    for i in range(len(x)):
        if a>x[i] and a<x[i+1]:
            return( y[i]+(a-x[i])*dif(i,i+1))
        if a==x[i] :
            return y[i]
x=linspace(1,10,20)
y=[]
for i in range(len(x)):
    y.append(f(x[i]))
plot(x,y)
z=input("enter any value between 1 and 10")
print "value is:", inte(z)
print"real value is;",f(z)
plot(z,inte(z),'ro')
show()
