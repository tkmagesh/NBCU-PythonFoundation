""" 
maintain a collection of products
product attributes
    id
    name
    cost
    units
    in_stock
Print the products
Calculate the over all stock value for in-stock products and print it
    sum(cost * units)
"""

p1 = (101, "Pen", 5, 20, True)
p2 = (102, "Pencil", 2, 50, False)
p3 = (103, "Marker", 50, 10, True)
p4 = (104, "Scribble-Pad", 30, 25, True)

""" 
products = []
products.append(p1)
products.append(p2)
products.append(p3)
products.append(p4) 
"""

products = [p1, p2, p3, p4]

stock_value = 0

""" 
for p in products:
    # print(f"id = {p[0]}, name = {p[1]}, cost = {p[2]}, units = {p[3]}")
    id, name, cost, units = p # unpacking
    print(f"id = {id}, name = {name}, cost = {cost}, units = {units}")
    product_value = cost * units
    stock_value += product_value 
"""

""" 
product_values = []

for id, name, cost, units in products:
    print(f"id = {id}, name = {name}, cost = {cost}, units = {units}")
    product_value = cost * units
    product_values.append(product_value)

print(f"product values : {product_values}")
stock_value = sum(product_values) 
"""

# transform the product list into a list of product values
product_value_list = [cost * units for id, name, cost, units, in_stock in products if in_stock]

# aggregate the product value list
stock_value = sum(product_value_list)

# transform the product list into a list of strings for printing
product_list_str = [f"id = {id}, name = {name}, cost = {cost}, units = {units}, in-stock = {in_stock}" for id, name, cost, units, in_stock in products if in_stock]

# append the list of strings with a new line (\n)
product_list_output = "\n".join(product_list_str)

# print everything
print("In Stock products list:")
print(product_list_output)
print(f"Stock value (In Stock) : {stock_value}")

