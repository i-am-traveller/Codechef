t=int(input());
for i in range(t):
    q,p=map(int,input().split());
    p=float(p);
    tot=0.0;
    if(q>1000):
        tot=q*p;
        tot-=0.1*tot;
    else:
        tot=q*p;
    print("%.6f"%tot);