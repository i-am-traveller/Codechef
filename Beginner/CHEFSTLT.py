t=int(input());
for i in range(t):
    s1=input();
    s2=input();
    mn,mx=0,0;
    for i in range(len(s1)):
        if(s1[i]!="?" and s2[i]!="?" and s1[i]!=s2[i]):
            mn+=1;
        elif(s1[i]=="?" or s2[i]=="?"):
            mx+=1;
    mx+=mn;
    print(mn,mx);
