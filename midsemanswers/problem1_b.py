'''Jai Kumar Roll no. 15076'''
'''problem 1(b)'''
'''i have taken square of radius 1 and only 1/4th of circle is inside the square'''
from random import *
#print random()
ac=0 #area of cirle
asq=0 #area of square
for i in range(100000):
    x=random()
    y=random()
    if(x**2+y**2<1):
        ac=ac+1 #total number of dots inside the circle
    else:
        asq=asq+1
print "Area of circle is:",ac*1.0/(ac+asq)
print "Value of pie is:",ac*4*1.0/(ac+asq) #since square will inscribe only 1/4th of the circle
