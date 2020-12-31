#Program for Center of mass in 2-D
#Swadhin Agrawal (Roll: 15223)
a=[]															#1-D Array for Mass 
print "Please enter the number of objects: ",
n=input()														#No. of Masses in space
b=[[] for i in range(11)]											#2-D Array for 2-D Coordinates
for i in range(1,n+1,1):
	print "Please enter the mass of the object %d : "%(i),
	a.append(input())												#Takes Mass of i'th object 
	print "Please enter the 3-D Co-ordinate(x,y,z) of the object %d : "%(i)	
	for j in range(2):	
		if j==0:
			print"X= ",
		else:
			print"Y= ",												
		b[i].append(input())										#Takes Co-ordinate of i'th object
print "\n"	
for i in range(n):												#Prints Data
	print "[Mass, (x,y,z)] = ",a[i],",",b[i+1]
k=0
s=[0,0]
for i in range(n):
	k=k+a[i]													#Sum of all the Masses 
	for j in range(2):					#Add's position's multiplied with respective Mass co-ordinate wise 
		s[j]=s[j]+a[i]*b[i+1][j]	
for j in range(2):						
	s[j]=float(s[j])
	s[j]=s[j]/k							#Calculates Center of Mass in 2-D
print "Hence, Center of Mass of all given objects is at = ","Mass= ",k,"Kg ,Coordnate= ",s,"meter"	#Prints Result
