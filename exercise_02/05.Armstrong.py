lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
 
for num in range(lower,upper + 1):
   sum = 0
   currentNum = num

   while currentNum > 0:
       digit = currentNum % 10
       sum += digit ** 3
       currentNum //= 10
 
   if num == sum:
       print(num)