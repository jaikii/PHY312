'''module to find area using simpson rule'''
'''Jai Kumar 15076'''
from matplotlib.pylab import *
from func import f
'''you have to give limits of x uper and lower to compute area'''
def simp(f,t,z):
    a=0
    x=linspace(t,z,1001)
    h=x[3]-x[2]
    for i in range(len(x)/2-1):
        a=a+(h*(f(x[2*i])+f(x[2*i+1])+f(x[2*i+2]))/3)
    return a

