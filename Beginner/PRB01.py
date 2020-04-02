import math;

def isPrime(n):
    point=int(math.sqrt(n));
    for i in range(2,point+1):
        if(n%i==0):
            return False;
    return True;

t=int(input());
for i in range(t):
    num=int(input());
    if(isPrime(num)):
        print("yes");
    else:
        print("no");