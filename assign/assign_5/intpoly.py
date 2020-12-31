from matplotlib.pylab import *
from math import sin,pi
def f(x):
    return(x**2+x+1)
def trapf(x,y):
	return(x-y)*(f(x)+f(y))/2
def simf(x,y,z):
    return(f(x)+4*f(y)+f(z))
x=[]
y=[]
z=[]
w=0
a=0
x=linspace(0,10,10001)
for i in xrange(len(x)-1):
    w=w+trapf(x[i+1],x[i])
print "Area using trapazoid rule is:", w
for i in xrange(len(x)/2):
    a=a+simf(x[2*i],x[2*i+1],x[2*i+2])
print "Area using simpson rule is:",a*(x[3]-x[2])/3
for i in xrange(len(x)-1):
	y.append(trapf(x[i+1],x[i]))
	#x.append(i)
        z.append(sin(x[i]))
y.append(0) #to make the index equal
plot(x,y)
xlabel("x")
ylabel("inte(f(x))")
savefig("int(f(x)).pdf")
show()
