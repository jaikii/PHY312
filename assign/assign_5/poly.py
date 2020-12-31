from matplotlib.pylab import *
from math import sin,pi
def f(x):
    return(x**2+x+1)
def df(x,y):
    return((f(y)-f(x))/(y-x))
x=[]
y=[]
z=[]
x=linspace(0,5,1001)
for i in xrange(len(x)-1):
	y.append(df(x[i+1],x[i]))
	#x.append(i)
        #z.append(f(x[i]))
y.append(0)
plot(x,y)
xlabel("x")
ylabel("d/dx(f(x))")
savefig("df.pdf")
show()
