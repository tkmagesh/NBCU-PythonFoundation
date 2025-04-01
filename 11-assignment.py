""" 
Refactor the below code to follow (SRP)    
"""

while True:
    print("""
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    """)
    user_choice = input("Enter your choice : ")
    if user_choice == '1':
        operand_1 = int(input("Enter operand 1 :"))
        operand_2 = int(input("Enter operand 2 :"))
        result = operand_1 + operand_2
        print(result)
    elif user_choice == '2':
        operand_1 = int(input("Enter operand 1 :"))
        operand_2 = int(input("Enter operand 2 :"))
        result = operand_1 - operand_2
        print(result)
    elif user_choice == '3':
        operand_1 = int(input("Enter operand 1 :"))
        operand_2 = int(input("Enter operand 2 :"))
        result = operand_1 * operand_2
        print(result)
    elif user_choice == '4':
        operand_1 = int(input("Enter operand 1 :"))
        operand_2 = int(input("Enter operand 2 :"))
        result = operand_1 / operand_2
        print(result)
    elif user_choice == '5':
        print("Thank you!")
        break
    else:
        print("Invalid choice!")