a,b=input().split()
lower = int(a)
upper = int(b)
for num in range(lower + 1,upper):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num,end= " ")
