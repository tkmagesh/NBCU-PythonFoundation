""" 
Build an interactive calculator

When the program is executed display the following menu:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Accept the user's choice
If the user's choice = 1 to 4
    Accept two operands from the user
    Perform the corresponding operation
    Print the result
    (*) Display the menu again
If the user's choice = 5
    Print "Thank you!"
    exit from the application
If the user's choice is NOT 1 to 5:
    Print "Invalid choice"
    (*) Display the menu again
    
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