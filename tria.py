try:
  n=int(input())
  s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in range(1,n+1):
    for j in range(1,n-i+1):
      print(" ",end=" ")
    for k in range(1,i+1):
      print(s[i-k],end=" ")
    print()
  for i in range(1,n):
    for j in range(0,i):
      print(" ",end=" ")
    l=n-i-1
    while(l>=0):
      print(s[l],end=" ")
      l-=1
    print()
except:
  print("exception")
