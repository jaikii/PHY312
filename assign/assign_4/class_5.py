from random import *
class mf():
    def __init__(self,amount,lo_intrest,emi):
        z= uniform(1,2)
        self.amount=amount
        self.z=z
        self.lo_intrest=lo_intrest
        self.emi=emi
    def md_r(self):
        t=0
        i=self.amount
        while i>=0 and i<=self.amount:
            i=(i*(1+self.lo_intrest/36000.0)**30)-self.emi 
            t=t+1
	self.t=t
        return(self.amount*(1+self.z/36000.0)**30*self.t)
def test():
    A=mf(1200000,8.5,15000)
    z=A.md_r()
    print "Amount after ",A.t," months is ",z," rupees after investing in mutual funds"
if __name__=='__main__':
    test()
    
        

    
