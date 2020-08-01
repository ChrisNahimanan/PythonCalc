print("Loading...")

Process = 0
while Process <= int(100):
    print(Process, "% Complete.")
    Process += int(10)
print("Process Finished.")
print("                     ")
print("Opening... Calculator 2.0")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

oP = input("Please choose an operator between 1-4: ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))

if oP == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif oP == "2":
    print(num1, "-", num2, "=", sub(num1, num2))
elif oP == "3":
    print(num1, "*", num2, "=", mult(num1, num2))
elif oP == "4":
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("Please enter a valid input.")
