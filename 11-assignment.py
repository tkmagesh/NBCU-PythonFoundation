""" 
Refactor the below code to follow (SRP)    
"""

def get_user_choice():
    print("""
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    """)
    user_choice = input("Enter your choice : ")
    return user_choice

def get_operands_v0():
    operand_1 = int(input("Enter operand 1 :"))
    operand_2 = int(input("Enter operand 2 :"))
    return operand_1, operand_2

def get_operands():
    data = input("Enter the operands (separated by \",\") : ")
    values = data.split(",")
    operand_1 = int(values[0].strip())
    operand_2 = int(values[1].strip())
    return operand_1, operand_2

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def perform_add():
    operand_1, operand_2 = get_operands()
    result = add(operand_1, operand_2)
    print(result)

def perform_subtract():
    operand_1, operand_2 = get_operands()
    result = subtract(operand_1, operand_2)
    print(result)


def perform_multiply():
    operand_1, operand_2 = get_operands()
    result = multiply(operand_1, operand_2)
    print(result)

def perform_divide():
    operand_1, operand_2 = get_operands()
    result = divide(operand_1, operand_2)
    print(result)


def App():
    while True:
        user_choice = get_user_choice()
        if user_choice == '1':
            perform_add()
        elif user_choice == '2':
            perform_subtract()
        elif user_choice == '3':
            perform_multiply()
        elif user_choice == '4':
            perform_divide()
        elif user_choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

App()