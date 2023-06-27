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

