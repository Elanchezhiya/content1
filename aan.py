o=input()
g1=g2=0
for i in o:
    if(i.isnumeric()):
        g1+=1
    elif(i.isalpha()):
        g2+=1
if(g1>=1 and g2>=1):
    print("Yes")
else:
    print("No")
