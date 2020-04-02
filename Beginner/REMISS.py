t=int(input());
for i in range(t):
    a,b=map(int,input().split());
    mx=a if(a>b) else b;
    print(mx,(a+b));
