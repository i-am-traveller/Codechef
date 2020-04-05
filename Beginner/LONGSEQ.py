t=int(input());
for i in range(t):
    s=input();
    l=len(s);
    c0=s.count("0");
    c1=s.count("1");
    if(c0==l-1 and c1==1):
        print("Yes");
    elif (c1 == l - 1 and c0 == 1):
        print("Yes");
    else:
        print("NO");