from interest import *
from random import *
'''
rd and mf money deposit
'''
print "Name: Jai Kumar, Roll no.: 15076 "
def present_amount(A0, p, n):
    return A0*(1 + p/(360.0*100))**n
def mf(): 
	print"(Mutual funds)"
	n=input("how would you like to pay the money(1:daily, 2:bi-monthly, 3: monthly, 4:half-yearly, 5: yearly")
	A=input("how much money you want to pay according to your plan")
	r= float(uniform(5,10))
	print "%f is the rate that you will be having on your deposit"%r
	z=mf_out(A,r,n)
	print z," is the amount you will be geeting at the end of the term"
	return(z)
def mf_out(A0,r,n):
	x=input("how many days you want to keep your money(360 days in a year)")
	if(n==1):
		A=A0
		for i in range(x):			
			A=A0+present_amount(A,r,n)
	if(n==2):
		A=A0
		for i in range(x/15):
			A=A0+present_amount(A,r,15)
	if(n==3):
		A=A0
		for i in range(x/30):
			A=A0+present_amount(A,r,30)
	if(n==4):
		A=A0
		for i in range(x/180):
			A=A0+present_amount(A,r,180)	
	if(n==5):
		A=A0
		for i in range(x/360):
			A=A0+present_amount(A,r,360)
	return(A)
def rd():
	print"(Recurring Deposit)"
	A0=input("How much money you want to pay mothly")
	r=6.5
	print"you will be getting %f rate on your deposit"%r
	x=input("how many days you want to keep your money(360 days in a year)")
	A=A0
	for i in range(x/30):
		A=A0+present_amount(A,r,30)
	print A," is your final amount"
	return(A)
#x=input("HEY !! WHat you wanna do with your money(1:mutual fund, 2:Reccuring fund)")
#if x==1:
print"Lets see which one is better for you"
m=mf()
#if x==2:
r=rd()
if r>m :
	print"Recurring deposit is a good option"
else:
	print"Mutual funds are better" 
