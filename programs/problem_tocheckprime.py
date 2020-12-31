x=input("Enter the number you want to ckeck is prime number(>2)")
n=x

y=2
z=0
while y!=n:
	if(n%y!=0):	
		y=y+1
		z=z+1
	else:
		break
if(z==n-2):
	print "yes"
else: print "no"
