t=int(input());
for i in range(t):
    s1=input();
    s2=input();
    flag=True;
    for j in range(len(s1)):
        if(s1[j]!="?" and s2[j]!="?" and s1[j]!=s2[j]):
            flag=False;
            break;
    if(flag):
        print("Yes");
    else:
        print("No");