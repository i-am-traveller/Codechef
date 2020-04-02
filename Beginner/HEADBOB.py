t=int(input());
for i in range(t):
    n=input();
    sign=input();
    if("I" in sign):
        print("INDIAN");
    else:
        if("Y" in sign):
            print("NOT INDIAN");
        else:
            print("NOT SURE");