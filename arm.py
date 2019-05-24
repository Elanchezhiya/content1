n=int(input())
x=list(map(int,str(n)))
y=list(map(lambda x:x**3,x))
if(sum(y)==n):
    print("yes")
else:
    print("no")
