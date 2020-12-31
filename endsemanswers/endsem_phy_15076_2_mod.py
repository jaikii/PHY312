from math import *
from matplotlib.pylab import *
m=1.0
def f(t):
    return m*(t%pi)



#part 2(a)

print"2(a)\n\n"
t=linspace(-1*5*pi,5*pi,1000)
y=[]
for i in range(len(t)):
    y.append(f(t[i]))
plot(t,y,label='f(t)',color='red')
xlabel("t")
ylabel("y")
show()


#part 2(b)
    
print"\n\n2(b)"
T=t[2]-t[1]
w= 2*pi/T
def dg(j,o,u):
    return u*e**(complex(0,(m+j)*w*o))
def rg(j,i):                         # using runge kutta method to sole the integral
    c1=T*dg(j,t[i],f(t[i]))
    c2=T*dg(j,t[i]+T/2,f(t[i])+c1/2)
    c3=T*dg(j,t[i]+T/2,f(t[i])+c2/2)
    c4=T*dg(j,t[i]+T,f(t[i])+c3)
    return (g1[j-1] + (c1+c2+c2+c3+c3+c4)/6)/T
j=1
z=[]
g1=zeros(200)
m=-100
for i in range(len(t)):
    l=1
    s=0.0
    while(l<200):
        g1[l]=rg(l,i)
        l+=1
    for k in range(len(g1)):
        s=s+ g1[k]*e**(complex(0,(m+k)*w*t[i]))
    z.append(s)
#part 2(c)


plot(t,z,label='Ff(t)',color='blue')
show()

'''sir if i am plotting the graph of both in same plot i am just getting forier trandformed graph i.e blue(no trace of red,i.e normal function graph) but if i am ploting the graph of normal function after hiding forier transformed i am getting graph of normal function, range of x and y values are also same in both the graps, i don't know the reason of this, so i am ploting the graph seperately'''
