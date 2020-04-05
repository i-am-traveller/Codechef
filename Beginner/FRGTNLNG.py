t=int(input());
for i in range(t):
    dsize,n=map(int,input().split());
    dct=list(map(str,input().split()));
    exist=[0]*dsize;
    for j in range(n):
        ls=list(map(str,input().split()));
        for k in ls[1:]:
            if(k in dct):
                index=dct.index(k);
                exist[index]=1;
    for j in exist:
        if(j==1):
            print("YES",end=" ");
        else:
            print("NO",end=" ");
    print();
