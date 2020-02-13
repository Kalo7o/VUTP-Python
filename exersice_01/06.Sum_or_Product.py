n = int(input("Type a number: "))

option = int(input("Type option 1-SUM or 2-MULTIPLY: "))

if option == 1:
    print(sum(range(1, n + 1)))
if option == 2:
    product = 1
    for i in range(1, n + 1):
        product = product * i
    print(product)
