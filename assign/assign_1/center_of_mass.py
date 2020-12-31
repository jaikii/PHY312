print"Name: Jai Kumar Roll no.:15076\n problem 1:Center of mass"
x=[[2,'kg'],[0,10],[3,'kg'],[10,1],[7,'kg'],[2,2],[4,'kg'],[3,7],[1,'kg'],[4,9],[12,'kg'],[-3,5],[9,'kg'],[0,-5],[2,'kg'],[-9,0],[9,'kg'],[6,9],[7,'kg'],[3,-7]]
i=0
l=0.0
m=0.0
n1=0.0
while i<20:
    j=0
    while j<=1:
        if x[i][1]=='kg':
            n1=n1+x[i][0]
            break
        else:
            if j==0:
                l=l+(x[i-1][0]*x[i][j])
            if j==1:
                m=m+(x[i-1][0]*x[i][j])
        j=j+1
    i=i+1
print "Center of mass is:[",l/n1,"m,",m/n1,"m]"
