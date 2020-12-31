'''write=open('data','w')
x=raw_input("Write a story: ")
#for i in range(len(x)):
	#write.write('%s' %x[i])
write.write("%s" %x)
write.close()'''
def count():
	jk=open('data','r')
	line=[]
	i=0
	for l in jk:
		while i<len(l):
			line.append(l[i])
			i=i+1
	jk.close()
		
	return(line)
y=count()
print y
x=raw_input("which word you want to find")
s=0
for i in range(len(y)):
	if y[i]==x:
		s=s+1
print s
jk=open('data','r')
jk.readline()
z=[]
for i in jk:
	print i
	k=i.split()
	z.append(float(k[1]))
	print z

