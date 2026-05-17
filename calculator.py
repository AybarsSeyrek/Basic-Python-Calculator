# Python calculator

operator = input("Enter an operator (+ - * /): ") #asks the user for arithmetic operator

try: # try / except is used to handle errors so the program does not crash.
    num1 = float(input("Enter the 1st number: ")) # to avoid string concatenation use Type casting (turn string to float)
    num2 = float(input("Enter the 2nd number: "))

    if operator == "+":
        result = num1 + num2
        print(round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print(round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print(round(result, 3))
    elif operator == "/":
        if num2 == 0:
            print("You cannot divide by zero")
        else:
            result = num1 / num2
            print(round(result, 3))
    else:
        print(f"{operator} is not valid operator")
except ValueError: 
    print("Invalid number. Please enter a real number.")
