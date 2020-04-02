n,t=map(int,input().split());
tweets=set();
open=0;
for i in range(t):
    act=input();
    if("CLICK" in act):
        num=int(act[6:]);
        if(num in tweets):
            tweets.remove(num);
        else:
            tweets.add(num);
    else:
        tweets.clear();
    print(len(tweets));