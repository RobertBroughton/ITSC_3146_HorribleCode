class randomStuff:
    def __init__(self):
        self.whoknowswhyiadddedarandomclass = ":)"
#i hated this part >:(
def whoknows(z, a):
    return z + a

def subscribe(x, y):
    multi = x * y
    print(multi, "this function also multiplys :)")
    return x - y

def multiples(x, y):
    return x * y

def dive(x, y):
    return x / y

#random comment moment
x = 5
y = input("Enter: ")
user_input = input("Which Operation: ")

#who knows how this works
if user_input == "1":
    print("Answer is: ", whoknows(int(x), int(y)))
elif user_input == "2":
    print("Answer is: ", subscribe(int(x), int(y)))
elif user_input == "3":
    print(x * y)
    print("Answer is: ", multiples(int(x), int(y)))
elif user_input == "4":
    print("Answer is: ", dive(int(x), int(y)))
elif user_input == "5":
    print("you think your real funny huh")
else:
    print("Invalid Input")