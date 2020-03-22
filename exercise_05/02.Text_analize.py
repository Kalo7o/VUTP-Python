string = input("Enter the stringing : ")

vowels = 0
digits = 0
consonants = 0
spaces = 0
symbols = 0

string = string.lower()

vowels_list = ['a', 'e', 'i', 'o', 'u']
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(0, len(string)):
    if(any(ele in string[i] for ele in vowels_list)):
        vowels = vowels + 1
    elif(any(ele in string[i] for ele in number_list)):
        digits = digits + 1
    elif(string[i] == ' '):
        spaces = spaces + 1
    elif(string[i].isalpha()):
        consonants = consonants + 1
    else:
        symbols = symbols + 1

print("Vowels: ", vowels)
print("Consonants: ", consonants)
print("Digits: ", digits)
print("White spaces: ", spaces)
print("Symbols : ", symbols)
