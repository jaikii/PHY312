from matplotlib.pylab import *
import numpy as np
A=np.array([[1,2,0],[3,1,0],[0,4,1]])
B= np.array(A)
C= np.array(A)
D= [[1,2,3],[1,2]]
print np.asarray(A)
print np.asarray(B+C)
print np.asarray(B*(B+C))
print np.ndim(A)
X=list(np.shape(A))
print X
print np.size(A)
print type(A)
x=np.linspace(0,2*(np.pi),99)
y=np.sin(x)
'''print x
print y
plot(x,y)
xlabel("x")
ylabel("sinx")
show()
'''
print A.dot(B+C)
#print A.dot(D)
#print np.arange(0,np.pi,dtype=float)
print A.T
