t=int(input());
for i in range(t):
    n=int(input());
    miss=[];
    for j in range(n):
        cur=int(input());
        if(cur in miss):
            miss.remove(cur);
        else:
            miss.append(cur);
    print(miss[0]);