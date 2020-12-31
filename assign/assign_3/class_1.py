class mona:
    def __init__(self,loan,interest,emi):
        self.loan=loan
        self.interest=interest
        self.emi=emi
    def time(self):
        i=self.loan
        t=0
        while i>=0 and i<=self.loan:
            i=i*((1-self.interest/36000.0)**30)-self.emi
            t=t+1
        return t
#z=mona(1200000,8.5,15000)
#val=z.time()
#print val

            
