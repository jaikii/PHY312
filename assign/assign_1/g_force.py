print"Name: Jai Kumar Roll no.:15076"
import pprint as pp
def sq(a,b): #to find distance between two vectors a and b
	return((a[0]-b[0])**2+(a[1]-b[1])**2)
j=input("How many point masses you have")
ms=0.0
y=0.0
i=0
x1=y1=z1=0.0
m=[]
p=[]
for i in range(j):
	print"Enter the mass of %d :" %(i+1)
	n=input()
	ms=ms+n
	m.append(n) #m is lis of masses
	print"Enter x,y coordinates: "
	x=input()
	y=input()
	#z=input()
	p.append([x,y])	# p is the list of postion vectors
print m
pp.pprint(p)
for i in range(j):
	g=0.0
	for k in range(j):
		if i==k:
			continue
		else:
			g=g+m[i]*m[k]*1.0/sq(p[i],p[k])
	print "gravitational force due to %d mass is :" %(i+1),g
