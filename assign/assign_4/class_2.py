class lon():
    def __init__(self,loan,emi,lo_intrest,fd_intrest):
        self.loan=loan
        self.emi=emi
        self.lo_intrest=lo_intrest
        self.fd_intrest=fd_intrest
    def fd_return(self):
            t=0
            i=self.loan
            while i>=0 and i<=self.loan:
                i=(i*(1+self.lo_intrest/36000.0)**30)-self.emi
                t=t+1
            self.t=t
            return(self.loan*(1+self.fd_intrest/36000.0)**(30*self.t))

def test():
    k=lon(1200000,15000,8.5,6.5)
    #x=k.tm()
    y=k.fd_return()
    print "time took to pay loan",k.t," and money in fd is ",y
if __name__=='__main__':
    test()
        
