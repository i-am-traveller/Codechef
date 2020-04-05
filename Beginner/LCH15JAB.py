t=int(input());
for i in range(t):
    st=input();
    stlen=len(st);
    visit=set();
    flag=False;
    for char in st:
        if(char in visit):
            continue;
        else:
            visit.add(char);
            cnt=st.count(char);
            if(cnt==stlen-cnt):
                flag=True;
                break;
    if(flag):
        print("YES");
    else:
        print("NO");
