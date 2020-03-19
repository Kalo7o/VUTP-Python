data_list = []
new_list = []

while True:
    currentInput = input('Enter some numbers and type "END" when you are done: ')
    if currentInput =='END':
        break
    else:
        data_list.append(currentInput)

while data_list:
    minimum = data_list[0]
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print(new_list)