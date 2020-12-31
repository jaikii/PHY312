from matplotlib.pylab import *
from math import sin,pi
def f(x,y):
	return(sin(y)-sin(x)/(y-x))
x=[]
y=[]
z=[]
x=linspace(0,5,10001)
for i in xrange(len(x)-1):
	y.append(f(x[i],x[i+1]))
	#x.append(i)
        z.append(sin(x[i]))
y.append(0)
plot(x,y)
xlabel("x")
ylabel("d/dx(sinx)")
savefig("cos.pdf")
show()
z.append(sin(5))
plot(x,z)
xlabel("x")
ylabel("sin(x)")
show()
