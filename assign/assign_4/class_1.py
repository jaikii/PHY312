class lon():
    def __init__(self,loan,emi,lo_intrest,fd_intrest):
        self.loan=loan
        self.emi=emi
        self.lo_intrest=lo_intrest
        self.fd_intrest=fd_intrest
    def tm(self):
        t=0
        i=self.loan
        while i>=0 and i<=self.loan:
            i=(i*(1+self.lo_intrest/36000.0)**30)-self.emi
            t=t+1
        return(t)
    def fd_return(self,tm):
        return(self.loan*(1+self.fd_intrest/36000.0)**(30*tm))
j=lon(1200000,15000,8.5,6.5)
z=j.tm()
y=j.fd_return(z)
print y,z
class fd():
    def __init__(self,amount,emi,intrest,tm):
        self.amount=amount
        self.emi=emi
        self.intrest=intrest
        self.tm=tm
    def rd(self):
        k=0
        for i in range (self.tm):
            k=self.emi+k*(1+self.intrest/36000.0)**30
        return(k)
k=fd(1200000,15000,6.5,z)
x=k.rd()
print x
print y-x
