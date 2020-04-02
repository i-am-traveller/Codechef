def reverse(n):
    rev=0;
    while(n!=0):
        x=n%10;
        rev=(rev*10)+x;
        n//=10;
    return rev;

t=int(input());
for i in range(t):
    n=int(input());
    print(reverse(n));