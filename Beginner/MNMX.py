t=int(input());
for i in range(t):
    n=input();
    ls=list(map(int,input().split()));
    cost=int(min(ls))*(len(ls)-1);
    print(cost);
