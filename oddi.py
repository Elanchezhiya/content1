a,b = input().split()
start=int(a)
end=int(b)
for num in range(start, end + 1): 
	if num % 2 != 0: 
		print(num, end = " ") 
