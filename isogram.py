str=input().split()
for o in str:
    st=set(o)
    if(len(st) == len(o)):
        print("Yes")
    else:
        print("No")
