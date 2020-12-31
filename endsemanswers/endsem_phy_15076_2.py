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



#part 2(b)

print"\n\n2(b)"
T=t[2]-t[1]
w= 2*pi/T
def g(j,i):
    return f(t[i])*e**(complex(0,j*w*t[i]))*T/(T)
z=[]
for i in range(len(t)):
    j=-100
    s=0
    while j<100:
        s=s + g(j,i)*e**(complex(0,j*w*t[i]))
        j+=1
    z.append(s)
#part 2(c)


plot(t,z,label='Ff(t)',color='blue')
show()
''' in this i dont know why i was getting 'scaled' answer i thought problem was integration so i changed it and wrote another program'''
