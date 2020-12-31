class red():
    def __init__(self,amount,emi,lo_intrest,fd_intrest):
        self.amount=amount
        self.emi=emi
        self.fd_intrest=fd_intrest
	self.lo_intrest=lo_intrest
    def rd(self):
        t=0
        i=self.amount
        while i>=0 and i<=self.amount:
            i=(i*(1+self.lo_intrest/36000.0)**30)-self.emi 
            t=t+1
	self.t=t
	k=0
        for i in range (self.t):
            k=self.emi+k*(1+self.fd_intrest/36000.0)**30
        return(k)
def test():
    x=red(1200000,15000,6.5,8.5)
    #tm=x.tm()
    rd=x.rd()
    print"time took to pay the loan amount is ",x.t," amount after fixed deposit is ",rd
if __name__=='__main__':
    test()
    
