t=int(input());
price=[2048,1024,512,256,128,64,32,16,8,4,2,1];
for i in range(t):
    num=int(input());
    count=0;
    for j in range(len(price)):
        if(num==0):
            break;
        if(price[j]>num):
            continue;
        while(num>=price[j]):
            num-=price[j];
            count+=1;
    print(count);
