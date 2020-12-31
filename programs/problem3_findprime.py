x=input("Enter the number till you want to find prime numbers(>2)")
n=x

while n!=1: #to run from the selected number to 2
	y=2
	z=0
	while y!=n: #to check whether the number is prime or not 
		if(n%y!=0):	
			y=y+1
			z=z+1
		else:
			break
	if(z==n-2):
		print n
	n=n-1
