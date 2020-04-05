t=int(input());
for i in range(t):
    num=int(input());
    mx=-99;
    size=0;
    for j in range(1,num+1):
       if(num%j>=mx):
           mx=num%j;
           size=j;
    print(size);