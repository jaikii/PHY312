''' dy/dt=g,dg/dt=(k/m)y, initial value: at t=0,y=0,g=0'''
from matplotlib.pylab import *
y=[]
g=[]
t=[]
T=0.001
k=100
m=2
#initial values
y.append(2)
t.append(0)
g.append(0)
i=1
while(i<10000):
    g.append(g[i-1] - k*1.0*y[i-1]/m)
    y.append(y[i-1] + T*g[i-1])
    print g[i-1],y[i-1]
    t.append(T*i)
    #correction using iteration
    g[i]=g[i-1] + (y[i]+y[i-1])*T/2
    y[i]=y[i-1] - (g[i]+g[i-1])*T/2
    i=i+1
xlabel("t")
ylabel("y")
plot(t,y)
plot(t,g)
show()
