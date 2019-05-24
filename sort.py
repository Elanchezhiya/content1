n = int(input())
a = input() 
e = list(map(int,a.split(' '))) 
e.sort()
for i in range (n):
    print(e[i],end=" ")
