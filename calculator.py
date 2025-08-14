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
        print("Would you like to? ")
        print("""1. Add.
2. Subtract.
3. Multiply.
4. Divide.
5. Exit.""")
        operation = int(input("Choose an operation (1-5): "))
    except ValueError:
        print("\nTo choose an operation, enter the number assigned to the operation. \nTRY AGAIN.\n")
    except Exception as e:
        print(f"{e}\n")
    else:
        try:
            if operation == 1 or operation == 2 or operation == 3 or operation == 4:
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))
        except ValueError:
                print("\nPlease enter a valid numeric value.\n")
        except Exception as e:
            print(f"{e}\n")
        else:
            if operation == 1:
                add = sum(a, b)
                print(f"{a} + {b} = {add}\n")
            elif operation == 2:
                subtract = subtraction(a, b)
                print(f"{a} - {b} = {subtract}\n")    
            elif operation == 3:
                multiply = multiplication(a, b)
                print(f"{a} * {b} = {multiply}\n")    
            elif operation == 4:
                try:
                    divide = division(a, b)
                    print(f"{a} / {b} = {divide}\n")   
                except ZeroDivisionError: 
                    print("\nYou can't divide by zero.\n")
                except Exception as e:
                    print(f"{e}\n")
            elif operation == 5:
                break
            else:
                print("\nChoose a valid operation. \nTRY AGAIN. \n")
                continue
