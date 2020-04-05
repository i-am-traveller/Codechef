t=int(input());
for i in range(t):
    store=set();
    ls=list(map(int,input().split()));
    for j in ls:
        if(j in store):
            store.remove(j);
        else:
            store.add(j);
    print("YES") if(len(store)==0) else print("NO");