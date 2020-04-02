t=int(input());
for i in range(t):
    n,m,k=map(int,input().split());
    diff=int(abs(n-m));
    if(k>=diff):
        print(0);
    else:
        print(diff-k);