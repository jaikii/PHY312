print"Name: Jai Kumar Roll no.:15076"
import pprint as pp
j=input("How many point masses you have")
ms=0.0
y=0.0
i=0
x1=y1=z1=0.0
m=[]
p=[]
for i in range(j): #to get the input
	print"Enter the mass of %d :" %(i+1)
	n=input()
	ms=ms+n
	m.append(n) #m is the list of masses	
	print"Enter x,y coordinates: "
	x=input()
	y=input()
	#z=input()
	p.append([x,y])	# p is the list of coordinates of masses
print m
pp.pprint(p)
for i in range(j):	
	x1=x1+m[i]*p[i][0]
	y1=y1+m[i]*p[i][1]
#	z1=z1+m[i]*p[i][2]
print"Center of mass is at: X=",x1/ms,"m , Y=",y1/ms,"m"

