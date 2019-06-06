
o=input()
n=list(o)
length=len(n)
if(length%2!=0):
    n[length//2]="*"
else:
    n[length//2]="*"
    n[length//2-1]="*"
for i in n:
    print(i,end="")
