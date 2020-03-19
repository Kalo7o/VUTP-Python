print("input some numbers and type \"END\" when you done: ")

numbers = []

while True:
    currentInput = input()
    if currentInput =='END':
        break
    else:
        numbers.append(float(currentInput)) 

print("Largest number: ", max(numbers))
print("Smallest number: ", min(numbers))