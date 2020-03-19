def count_occurrencies(lst, n): 
    count = 0
    for ele in lst: 
        if (ele == n): 
            count = count + 1
    return count 
  

lst = [] 

while True:
    currentInput = input('Enter some things and type "END" when you are done: ')
    if currentInput =='END':
        break
    else:
        lst.append(currentInput)

n = input("Wich element you are searching for?: ")

print('{} has appeared {} times'.format(n, count_occurrencies(lst, n))) 