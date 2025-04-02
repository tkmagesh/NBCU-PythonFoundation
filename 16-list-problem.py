""" Create a python program which will keep accepting "product names" from the user until the user enters "done". When the user enters "done", print all the product names and exit the program """

products = []
while True:
    name = input("Enter the product name : ")
    if name == "done":
        print(f"{len(products)} products added!")
        print("Products List :")
        for product_name in products:
            print(product_name)
        break
    else:
        products.append(name)

""" 
1. Expand scope to "remove", "list", "search" the products
2. refactor the solution to functions (follow SRP)
 """
