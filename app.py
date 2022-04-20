welcome_text = "Welcome! This is my first calculator!"

print(f"{welcome_text}\n")

def addition():
    total = number1 + number2
    print(total)


def subtrace():
    total = number1 - number2
    print(total)


def multiply():
    total = number1 * number2
    print(total)


def division():
    total = number1 / number2
    print(total)
    

def square():
    total = squared_number * squared_number
    print(total)

select_mode = input("Type\nA to Addition\nS to Subtrace\nM to Multiply\nD to Division\nSQ to Square\n\n")

if select_mode == "SQ":
    squared_number = int(input("Enter the number whose square you want: "))

elif select_mode != "SQ":
    number1 = int(input("Enter the first number that you want to calculate with: "))
    number2 = int(input("Enter the second number that you want to calculate with: "))

if select_mode == "A":
    addition()

elif select_mode == "S":
    subtrace()

elif select_mode == "M":
    multiply()

elif select_mode == "D":
    division()

elif select_mode == "SQ":
    square()