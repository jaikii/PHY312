print"Name: Jai Kumar Roll no.:15076"
from math import sqrt
x=input("How many numbers you want to enter")
a=[]
s=0.0
for i in range(x): # to get the list of numbers
	n=input("Enter the number:")
	a.append(n)
	s=s+n
print a
y=0.0
for i in range(x): #to find the standard deviation i.e sqrt(sum of (x-xi)**2)
	y=y+(a[i]-(s/n))**2
print "standard deviation is:",sqrt(y/n)
	
