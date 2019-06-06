o=int(input())
k=0
for i in range(2,o//2+1):
    if(o%i==0):
        k=k+1
if(k<=0):
    print("yes")
else:
    print("no")
