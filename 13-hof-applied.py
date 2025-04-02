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

def perform_operation(op):
    operand_1, operand_2 = get_operands()
    result = op(operand_1, operand_2)
    print(result)

def App():
    while True:
        user_choice = get_user_choice()
        if user_choice == '1':
            # perform_operation(add)
            perform_operation(lambda x,y : x + y)
        elif user_choice == '2':
            # perform_operation(subtract)
            perform_operation(lambda x,y : x - y)
        elif user_choice == '3':
            # perform_operation(multiply)
            perform_operation(lambda x,y : x * y)
        elif user_choice == '4':
            # perform_operation(divide)
            perform_operation(lambda x,y : x / y)
        elif user_choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

App()