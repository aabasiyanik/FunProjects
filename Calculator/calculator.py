from calcascii import calculator
print(calculator)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


is2 = True
while is2:
    isValid = True
    while isValid:
        try:
            first_num = int(input("What's the first number?: "))

            is1 = True
            while is1:
                operation = input("+\n-\n*\n/\nPick an operation: ")
                if operation not in ['+', '-', '*', '/']:
                    print("\nPlease pick a valid operation!")
                elif operation in ['+', '-', '*', '/']:
                    is1 = False

            second_num = int(input("\n\nWhat's the next number?: "))
            isValid = False
        except ValueError:
            print("Something went wrong, please try again.\n\n\n")

        if operation == '+':
            result = add(first_num, second_num)
        elif operation == '-':
            result = subtract(first_num, second_num)
        elif operation == '*':
            result = multiply(first_num, second_num)
        elif operation == '/':
            result = divide(first_num, second_num)
        
        print(f"{first_num} {operation} {second_num} = {result}")

        is3 = True
        while is3:
            whatNext = input(f"\nType 'y' to continue calculating with {result}, or type 'n' to start a new calculation. Type 'q' to Quit: ")
            if whatNext.lower() not in ['y', 'n', 'q']:
                print("Please type 'y', 'n', or 'q'")
            else:
                is3 = False
        if whatNext.lower() == 'q':
            exit()
        elif whatNext.lower() == 'n':
            pass
        elif whatNext.lower() == 'y':
            while whatNext.lower() == 'y':
                is4 = True
                while is4:
                    operation1 = input("Pick an operation: ")
                    if operation1 not in ['+', '-', '*', '/']:
                        print("\nPlease pick a valid operation!")
                    elif operation1 in ['+', '-', '*', '/']:
                        is4 = False
                second_N = int(input("\n\nWhat's the next number?: "))
                if operation1 == '+':
                    result1 = add(result, second_N)
                elif operation1 == '-':
                    result1 = subtract(result, second_N)
                elif operation1 == '*':
                    result1 = multiply(result, second_N)
                elif operation1 == '/':
                    result1 = divide(result, second_N)
                print(f"{result} {operation1} {second_N} = {result1}")
                result = result1

                is4 = True
                while is4:
                    whatNext = input(f"\nType 'y' to continue calculating with {result1}, or type 'n' to start a new calculation. Type 'q' to Quit: ")
                    if whatNext.lower() not in ['y', 'n', 'q']:
                        print("Please type 'y', 'n', or 'q'")
                    else:
                        is4 = False
                        if whatNext.lower() == 'q':
                            exit()
                        elif whatNext.lower() == 'n':
                            break