import math;

t=int(input());
for i in range(t):
    ls=list(map(int,input().split()));
    count=ls[0];
    quant=ls[1:];
    gcd=quant[0];
    for i in quant[1:]:
        gcd=int(math.gcd(gcd,i));
    for i in quant:
        print(i//gcd,end=" ");
    print();