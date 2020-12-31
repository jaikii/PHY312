from math import log as ln
def loan_pay(A,rl,emi,tl):
	i=ci(A,rl,30)-A
	A=A-emi-i
	#print A
	if(A>=0):
		tl=tl+1
		loan_pay(A,rl,emi,tl)
	else:
		
		print tl/12,"years and ",tl-(tl/12)*12,"months \n" ,(-1)*A,"is the left amount after last payment"
		print ci(1200000,rd,87*30)
		return(tl/12,A)
		
		
def ci(A,r,t):
	return(A*(1+r/(360.0*100))**t)
def day(r,n):
	return(ln(n)/ln(1+(r/(360.0*100))))
def fix(emi,rd,t):
	y=emi
	for i in range(87):
		y=emi+ci(y,rd,30)
		#print y
	return(y)
A=1200000#input("Enter the initial amount")
t=86*30 #input("Number of days")
rd=6.5#input("Rate of interest for fixed diposit")
rl=8.5
emi=10000
z=loan_pay(A,rl,emi,0)
print z
print fix(emi,rd,t)

