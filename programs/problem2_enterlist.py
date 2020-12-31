x=list()
y=input("how many elements you want to enter")
i=0
while i!=y:
	n=input("enter the list")
	x.append(n)
	i=i+1
print x
z=input("which number you want to see")
print x[z-1]

