class mona1:
    def __init__(self,fd,interest,time):
        self.fd=fd
        self.interest=interest
        self.time=time
    def amount(self):
        x=self.fd*(1-self.interest/36000.0)**(self.time*30)
        return (x)
from class_1 import *
y=mona(1200000,8.5,15000)
t=y.time()
print t
z=mona1(1200000,6.5,t)
val=z.amount()
print val
