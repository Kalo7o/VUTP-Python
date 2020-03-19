print("Operations +, -, *, /")

num1 = int(input("Enter first number: "))
choice = input("Enter operation:")
num2 = int(input("Enter second number: "))


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


if choice == '+':
    print(num1, choice, num2, "=", add(num1, num2))

elif choice == '-':
    print(num1, choice, num2, "=", subtract(num1, num2))

elif choice == '*':
    print(num1, choice, num2, "=", multiply(num1, num2))

elif choice == '/':
    print(num1, choice, num2, "=", divide(num1, num2))

else:
    print("Invalid input")
