from matplotlib.pylab import *
def rad(x):
    return(7**5*x%(2**32-1))
x=[]
y=[]
for i in range(10000):
    x.append(i)
    y.append(i)
plot(x,y)
xlabel("x")
ylabel("random")
show()
