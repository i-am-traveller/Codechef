t=int(input());
for i in range(t):
    a,b=map(int,input().split());
    print("<") if(a<b) else print(">") if(a>b) else print("=");
    