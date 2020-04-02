def sum(n):
    sm=0;
    for i in range(1,n+1):
        sm+=i;
    return sm;

t=int(input());
for i in range(t):
    d,n=map(int,input().split());
    for i in range(d):
        n=sum(n);
    print(n);