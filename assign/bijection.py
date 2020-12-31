from math import *
def f(x):
    return (x-2)*(x+2)
a=float(input("Enter left hand limit"))
b=float(input("Enter right hand limit"))
print"limit is", 10E-4
while abs(a-b)>10E-4:
    if f(a)*f((a+b)/2)<0:
        b=(a+b)/2
        x= b
    else :
        a=(a+b)/2
        x=a
print "roots is at :",x
