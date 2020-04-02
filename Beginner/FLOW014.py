t=int(input());
for i in range(t):
    ls=list(map(str,input().split()));
    ha=int(ls[0]);
    cc=float(ls[1]);
    ts=int(ls[2]);
    if(ha>50 and cc<0.7 and ts>5600):
        print(10);
    elif(ha>50 and cc<0.7):
        print(9);
    elif(cc<0.7 and ts>5600):
        print(8);
    elif(ha>50 and ts>5600):
        print(7);
    elif(ha>50 or cc<0.7 or ts>5600):
        print(6);
    else:
        print(5);