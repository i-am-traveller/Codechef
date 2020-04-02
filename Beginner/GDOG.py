t=int(input());
for i in range(t):
    n,k=map(int,input().split());
    ls=[];
    for j in range(1,k+1):
        ls.append(n%j);
    print(max(ls));