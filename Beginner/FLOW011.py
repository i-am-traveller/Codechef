t=int(input());
for i in range(t):
    sal=int(input());
    hra=500 if(sal>=1500) else sal*0.1;
    da=0.98*sal if(sal>=1500) else 0.9*sal;
    gross=sal+hra+da;
    print("%.2f"%gross);