string = input("Enter string: ")

vowels = {}


for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        try:
            vowels[i] += 1
        except:
            vowels[i] = 1
        

print("Number of vowels are: ")

for key in vowels:
    print(key, '->', vowels[key])

