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
y.append(y[0] + T*g[0])# +T**2(dg0/dt + g[0]*dg0/dy)
g.append(g[0]-k*1.0*y[1]/m)
t.append(0.001)
i=2
while(i<100):
    y.append(y[i-2] + 2*T*g[i-1])
    g.append(g[i-1] - k*1.0*y[i-1]/m)
    y[i]=y[i-2] + T*(g[i]+4*g[i-1]+g[i-2])/3 
    print g[i-1],y[i-1]
    t.append(T*i)
    i=i+1
xlabel("t")
ylabel("y")
plot(t,y)
plot(t,g)
show()
