t=int(input());
den=[100,50,10,5,2,1];
for i in range(t):
    sum=int(input());
    count=0;
    j=0;
    while(sum!=0):
        if(sum>=den[j]):
            sum-=den[j];
            count+=1;
        else:
            j+=1;
    print(count);