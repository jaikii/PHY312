x=list()
y=input("how many elements you want to enter")
i=0
#to enter the list in x variable
while i!=y:
	n=input("enter the list")
	x.append(n)
	i=i+1
print x
#to arrange the numbers in the list
j=1
while (j!=y):
	i=j
	min_num=x[i-1]
	while(i!=0):
		if(x[i]<=min_num):
			x[i-1]=x[i]
			x[i]=min_num
		min_num=x[i-2]
		i=i-1	
	j=j+1	
print"arranged list is ",x
