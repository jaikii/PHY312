'''Jai Kumar 15076'''
from matplotlib.pylab import *
def f(x):
    return x**2
def delta(x,h):
    print h
    z = f(x+h)-f(x-h)/2*h
    return z
def tow(x,k,l):
    i=0
    if l==0:
        z=h/2**k
        return delta(x,z)
    else :
        return (((4**l*tow(x,k,l-1))/((4**l)-1))-(tow(x,k-1,l-1)/((4**l)-1)))
def B(k,l):
    if l==k:
        return 0
    else :
        return ((4**l-4**k)/(((4**l)-1))*B(k,l-1))
def dif(x):
    a=0
    if l==k:
        return tow(x,k,l)
    i=l+1
    while(i<50):#any large value can suffice
        a=a+(B(k,i)*((h/(2**k))**(2*i)))
        print a
        diff=tow(x,k,l)-a
    return(diff)
l=input("Enter the value of n")
k=l
x=linspace(1,10,101)
y=[]
z=[]
tk=[]
h=x[3]-x[2]
'''
for i in range(len(x)):
    y.append(f(x[i]))
    z.append(dif(x[i]))
print len(z)
#print z
plot(x,y)
plot(x,z)
'''
print dif(5)
print tow(5,0,0)
print ((f(5+0.05)-f(5-0.05))/0.1)
#show()

    
