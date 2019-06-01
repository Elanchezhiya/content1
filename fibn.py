x=int(input(""))
a=0
b=1
for i  in range(x):
    c=a+b
    a=b
    print(b,end=' ')
    b=c
