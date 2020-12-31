'''solution of oscillator in 2-D by use of runge kutta method dy/dt=g,dg/dt=-(k/m)y, initial value: at t=0,y=2,g=0 '''
from matplotlib.pylab import *
T=0.001
def G(y,t1,i):
    return (t1-t[i-2])*g[i-1]/T - (t1-t[i-1])*g[i-2]/T
def C(t,i):
    c.append(T*G(y[i-1],t,i))
    c.append(T*G(y[i-1] + c[0]/2 , t + T/2 , i))
    c.append(T*G(y[i-1] + c[1]/2 , t + T/2 , i))
    c.append(T*G(y[i-1] + c[2] , t + T  , i))
y=[]
t=[]
c=[]
g=[]
k=100
m=2
#initial values
t.append(0)
y.append(2)
g.append(0)
i=1
while(i<1000):
    t.append(T*i)
    g.append(g[i-1] - k*1.0*y[i-1]/m)
    C(t[i],i)
    y.append(y[i-1] + (c[0]+2*c[1]+2*c[2]+c[3])/6)
    i=i+1
for i in range(1000):
    print t[i] , y[i], g[i]
plot(t,y)
xlabel("t")
ylabel("y")
show()
