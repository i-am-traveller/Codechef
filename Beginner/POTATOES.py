import math;
def prime(n):
    sq=int(math.sqrt(n));
    for i in range(2,sq+1):
        if(n%i==0):
            return False;
    return True;

t=int(input());
for i in range(t):
    x,y=map(int,input().split());
    j=1;
    while(True):
        sm=x+y+j;
        if(prime(sm)):
            break;
        j+=1;
    print(j);