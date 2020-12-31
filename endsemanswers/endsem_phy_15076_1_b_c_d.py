import numpy as np
from math import sqrt
from endsem_phy_15076_1_a import trac,det,multi,trans


A=[[3,complex(2,-1),complex(0,-3)],[complex(2,1),0,complex(1,-1)],[complex(0,3),complex(1,1),0]]

P=[[-1/sqrt(7),complex(1/sqrt(728),-1*21/sqrt(728)),complex(1/sqrt(40),3/sqrt(40))],[complex(1/sqrt(7),2/sqrt(7)),complex(6/sqrt(728),-1*9/sqrt(728)),complex(-2/sqrt(40),-1/sqrt(40))],[1/sqrt(7),13/sqrt(728),5/sqrt(40)]]


'''for hermiticity AA*=I'''

def star(A):
    C=[]
    for i in range(len(A)):
        D=[]
        for j in range(len(A[0])):
            D.append(complex(A[i][j].real,(A[i][j].imag)*(-1)))
        C.append(D)
    return C

def dag(A):
    return trans(star(A))

def iden(J):
    k=0
    for i in range(len(J)):
        for j in range(len(J[0])):
            if i==j:
                if J[i][j]==complex(1.0,0.0):
                    k=1
            else:
                if J[i][j]==complex(0.0,0.0):
                    k=1
    return(k)


###part 1(b)
print"A=", A
print "1(b)\n\n"
print "determinant of A:",det(A)
print "Trace of A:",trac(A)
#Adag(A)-dag(A)A==0 for hermitian matrix
k=np.asarray(multi(dag(A),A)) - np.asarray(multi(A,dag(A)))
v=0
for i in range(len(A)):
    for j in range(len(A[0])):
        if k[i][j]==complex(0,0):
            v=1
if v==1:
    print "Matrix A is Hermitian"
else :
    print "Matrix A is not Hermitian"
###part 1(c)
print "P=",P
#if matrix is unitary U*U=I
print "\n\n1(c)\n\n"
J=multi(P,P)
#to check unitary
k=iden(J)
if(k==1):
    print "P is unitary"
else:
    print "P is not unitary"
                



###part 1(d)
print "\n\n1(d)\n\n"
X=multi(dag(P),A)
D=multi(X,P)
print "\nD=dag(P)AP :\n",D
print "\ntrace(D) :\n",trac(D)
print "\nDeterminant(D):\n",det(D)
