t=int(input());
for i in range(t):
    s=input();
    rev=s[::-1];
    if(s==rev):
        print("wins");
    else:
        print("losses");
