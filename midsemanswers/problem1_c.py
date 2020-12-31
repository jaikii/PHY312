'''Jai Kumar 15076'''
from simpson import simp
from matplotlib.pylab import *
def f(x,y,z):
    return sqrt(1-(x**2+y**2+z**2))
x=linspace(0,1,1001)
y=linspace(0,1,1001)
z=linspace(0,1,1001)
w=[]
t=[]
for i in xrange(len(x)):
    w.append(float(f(x[i],y[i],z[i])))




