
a,b = input().split()
start=int(a)
end=int(b)
for num in range( start + 1 ,end ): 
	if num % 2 == 0: 
		print(num, end = " ") 
