a=input()
d=0
b=len(a)
if (ord (a[0])<57):
    if(ord (a[0])>47 or ord (a[0])==45 or ord (a[0])== 46):
        for i in range (1,b):
            if(ord (a[i])>43 and ord (a[i])<58):
                d=1
            else:
                d=d-1
    else:
        d=d-1
else:
    d=d-1
if (d>0):
    print("yes")
else:
    print("No")
