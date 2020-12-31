def fixed(A,i,rd):
	return(A*((1+(rd/36000.0))**(i*30)))
def m_sav(emi,rd,tl):
	A=emi
	for i in range(tl):
		emi=A+fixed(emi,1,rd)
		#print emi
	return(emi)
A=input("Amount that you have initially to buy a car")
rl=input("Interest rate on loan")
rd=input("interest rate on fixed deposit")
emi=input("Monthly savings")
i=0
A0=A
while A>0:
	A=A*(1+rl/36000.0)**30-emi
	i=i+1
	#print A
	if(A>A0):
		print"Loan Amount can not be paid"
		break
if(A<A0):
	print"Amount paid for loan in",i/12,"years and ",(i/12.0-i/12)*12," months"
	f=fixed(A0,i,rd)
	print"Amount you will be having of fixed deposit will be ",f
	#m=m_sav(emi,rd,i)
	m=emi*i+A
	print"Amount you will be having by monthly savings will be",m
	print"Amount you saved by fixed deposit and taking loan is",f-m
