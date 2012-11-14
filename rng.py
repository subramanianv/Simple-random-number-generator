"""
This is code for a very simple random number generator linear congruential generator.
                     Xn=a*Xn-1 mod m
                     Xo= seed (usually system time)

Author     : Subramanian Venkatesan
Language   : Python
"""

import time
class RandomNumberGenerator:
    def __init__(self):
        self.randomints=[];
        self.count=0;
        self.a=1664525
        self.m=4294967296
        self.seed=time.mktime(time.gmtime()) # get epoch
    def rand(self): #generates a random number between 0 and 1
        if self.count==0:
           self.randomints.append((self.a*self.seed)%self.m)
        else:
           self.randomints.append((self.a*self.randomints[-1])%self.m)
	self.count+=1
        return self.randomints[-1]/self.m #return x/m to get x between 0 and 1
        
def main():
    x=RandomNumberGenerator()
    for i in range(0,5):
        print x.rand()
if __name__=="__main__":
    main()

