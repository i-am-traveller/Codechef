t=int(input());
for i in range(t):
    ls=list(map(int,input().split()));
    ls.sort();
    print(ls[1]);
