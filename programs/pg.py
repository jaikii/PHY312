print "jai"
s= list()
x=input("How many numbers you want to enter")
i=0
print"enter the list"
while(i!=x):
	y=input("")
	s.append(y)
	i=i+1
print s
j=1
while(j!=x):
	i=j-1
	key=s[j]
	while(i>=0 and s[i]>=key):
		s[i+1]=s[i]
		i=i-1
		s[i+1]=key
	j=j+1
print s
