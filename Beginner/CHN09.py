t=int(input());
for i in range(t):
    s=input();
    ca=s.count("a");
    cb=s.count("b");
    if(ca==0 or cb==0):
        print(0);
    else:
        print(min(ca,cb));