"""
This is code for a very simple random number generator linear congruential generator.
                     Xn=a*Xn-1 mod m
                     Xo= seed (usually system time)

Author     : Subramanian Venkatesan
Language   : Python
"""

import time
class RandomNumberGenerator:
    #constructor
    def __init__(self):
        self.randomints=[];
        self.count=0; # no of random numbers generated in the sequence.
        self.a=1664525
        self.m=4294967296 # 2^32
        self.seed=time.mktime(time.gmtime()) # get epoch
    
    # rand function
    def rand(self): 
        if self.count==0:
           # append X1=a*seed mod m
           self.randomints.append((self.a*self.seed)%self.m)
        else:
	   # append Xn=a*Xn-1 mod m
           self.randomints.append((self.a*self.randomints[-1])%self.m)
	#increment the count
	self.count+=1 
        return self.randomints[-1]/self.m #return x/m to get x between 0 and 1
        
def main():
    x=RandomNumberGenerator()
    for i in range(0,5):
        print x.rand()
if __name__=="__main__":
    main()

