print"Name: Jai Kumar Roll no.:15076"
from math import pi
def cir(r): #defination for finding area of circle
	return(pi*r**2)
def rec(a,b): #defination for finding area of rectangle
	return(a*b)
y=input("for circle press 1 for rectangle press 2\n")
if y==1:
	x=input("Enter the radius of cirlce\n")
	print"Area of circle is:",cir(x)
if y==2:
	a=input("Enter the length and breadth of rectangle\n")
	b=input()
	print"Area of rectangle is:",rec(a,b)


