t=int(input());
luck, unluck = 0, 0;
ls=list(map(int,input().split()));
for j in ls:
    if(j%2==0):
        luck+=1;
    else:
        unluck+=1;
if(luck>unluck):
    print("READY FOR BATTLE");
else:
    print("NOT READY");