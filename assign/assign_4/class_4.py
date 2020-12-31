from class_2 import *
from class_3 import *
x=input("Enter loan amount")
y=input("Enter the intrest rate of loan")
z=input("Enter the intrest rate of fd")
w=input("Enter monthly saving")
A=lon(x,w,y,z)
A_fd=A.fd_return()
if(A.t!=1):
	A=lon(x,w,y,z)
	A_fd=A.fd_return()
	print "Amount gain by taking loan of putting money in fd is",A_fd
	B=red(x,w,y,z)
	B_red=B.rd()
	print "Amount gain by rd",B_red
	print "profit made by taking loan",(A_fd-B_red)
else :
	print "Amount can never be paid"


