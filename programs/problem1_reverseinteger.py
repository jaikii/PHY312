c=input('write a number')
print"you have entered ",c
y=0
z=1
n=1
x=c
#to count the number of digits in the entered integer
while x/10!=0:
	a=x%10
	x=x/10
	n=n+1
	print x,n
#to reverse the number
while c/10!=0:
	b=c%10
	c=c/10
	y=y+b*(10**(n-1))
	n=n-1
y=y+c
print "number is now ",y
