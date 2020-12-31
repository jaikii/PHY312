print"Name: Jai Kumar Roll no.:15076"
import pprint
def vec(a,b): 
	d=0
	c=[]
	i=0
	while(i!=3):
		d=d+a[i]*b[i]  # to find scalar product
		if i==0:  # to find vector product
			c.append(a[i+1]*b[i+2]-a[i+2]*b[i+1])
		if i==1:
			c.append(a[i+1]*b[i-1]-a[i-1]*b[i+1])
		if i==2:
			c.append(a[i-2]*b[i-1]-a[i-1]*b[i-2])
		i=i+1
	return(d,c)
print"Enter first 3-D vector"
i=0
a=[]
b=[]
while(i!=3): # to get 1st vector
	n=input("")
	a.append(n)
	i=i+1
print"Enter seond 3-D vector"
j=0
while(j!=3): # to get 2nd vector
	n=input("")
	b.append(n)
	j=j+1
print"Scalar and vector products are"
z=vec(a,b)
pprint.pprint(z)


