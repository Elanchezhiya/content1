n = int(input())
a = input() 
e = list(map(int,a.split(' '))) 
for i in range (n):
    print(e[i],i)
