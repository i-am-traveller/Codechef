import math;

t=int(input());
for i in range(t):
    a,b=map(int,input().split());
    gc=int(math.gcd(a,b));
    lcm=(a*b)//gc;
    print(gc,lcm);