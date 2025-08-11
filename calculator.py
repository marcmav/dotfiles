def sum(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

while True:
    try:
        print("Choose operation (1-5):")
        print("""1. Add.
2. Subtract.
3. Multiply.
4. Divide.
5. Exit.""")
        operation = int(input("Would you like to? "))
    except ValueError:
        print("To choose an operation enter the number assigned to the operation. TRY AGAIN.\n")
    else:
        if operation == 1:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            add = sum(a, b)
            print(f"{a} + {b} = {add}")
        elif operation == 2:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            subtract = subtraction(a, b)
            print(f"{a} - {b} = {subtract}")    
        elif operation == 3:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            multiply = multiplication(a, b)
            print(f"{a} * {b} = {multiply}")    
        elif operation == 4:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            divide = division(a, b)
            print(f"{a} / {b} = {divide}")   
        elif operation == 5:
            break
        else:
            print("Chose a valid operation. TRY AGAIN. \n")
            continue
