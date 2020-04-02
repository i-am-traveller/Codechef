def factorial(n):
    if(n==0 or n==1):
        return 1;
    f=1;
    for i in range(2,n+1):
        f*=i;
    return f;

t=int(input());
for i in range(t):
    num=int(input());
    print(factorial(num));

