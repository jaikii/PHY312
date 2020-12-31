from matplotlib.pylab import *
from math import sin,pi
def trapf(x,y):
	return(x-y)*(sin(x)+sin(y))/2
def simf(x,y,z):
    return(sin(x)+4*sin(y)+sin(z))
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
y.append(0)
plot(x,y)
xlabel("x")
ylabel("int(sin(x))")
savefig("int(sin(x)).pdf")
show()
