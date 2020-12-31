'''module to calculate matrix operations'''

#multiplication

def multi(A,B):
    if len(A[0])!=len(B):
        print"Can't perform multiplication as matrix dimension despute"
    else :
        C=[]
        for i in range(len(A[0])):
            D=[]
            for j in range(len(B)):
                s=complex(0.0,0.0)
                for k in range(len(B[0])):
                    s=s+A[i][k]*B[k][j]
                D.append(s)
            C.append(D)
    return C


#trace

def trac(A):
    if len(A)!=len(A[0]):
        print "trace can not be found, dimension despute"
    else :
        s=complex(0.0,0.0)
        for i in range(len(A)):
            s+=A[i][i]
    return s



#transpose

def trans(A):
    D=[]
    for i in range(len(A)):
        C=[]
        for j in range(len(A[0])):
            C.append(A[j][i])
        D.append(C)
    return D


#determinant

def sub(A,m,n):
    D=[]
    for i in range(len(A)):
        C=[]
        f=0
        for j in range(len(A[0])):
            if i!=m and j!=n:
                C.append(A[i][j])
                f=1
        if f==1:
            D.append(C)
    return D
def det(A):
    if len(A)!=len(A[0]):
        print "Determinant can't be determine, dimension despute"
    else:
        if(len(A)==1):
            return A[0][0]
        else:
            s=complex(0.0,0.0)
            for i in range(len(A[0])):
                s+=(-1)**i * A[0][i] * det(sub(A,0,i))
    return s

'''
A=[[1,2],[4,3]]
B=[[2,3],[1,2]]
Z=[[2,0,0],[0,1,0],[0,0,5]]
print "matrices are:",A,B,Z
print "A*B",multi(A,B)
print "trace(Z)",trac(A)
print "transpose(Z)",trans(A)
print "determinant(Z)",det(Z)
'''
