#Basic Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#User Input
x = input("Enter First Number: ")
y = input("Enter Second Number: ")
user_input = input("Which Operation do you wish to perform?\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n")

#Operation Selection
if user_input == "1":
    print("Answer is: ", add(int(x), int(y)))
elif user_input == "2":
    print("Answer is: ", subtract(int(x), int(y)))
elif user_input == "3":
    print("Answer is: ", multiply(int(x), int(y)))
elif user_input == "4":
    print("Answer is: ", divide(int(x), int(y)))
else:
    print("Invalid Input")