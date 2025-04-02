""" 
Apply a discount(%) on the individual product
And calculate the stock value and print
"""

p1 = {"id" : 101, "name" : "Pen", "cost" : 5, "units" : 20, "in_stock" : True}
p2 = {"id" : 102, "name" : "Pencil", "cost" : 2, "units" : 50, "in_stock" : False}
p3 = {"id" : 103, "name" : "Marker", "cost" : 50, "units" : 10, "in_stock" : True}
p4 = {"id" : 104, "name" : "Scribble-Pad", "cost" : 30, "units" : 25, "in_stock" : True}

""" 
products = []
products.append(p1)
products.append(p2)
products.append(p3)
products.append(p4) 
"""

products = [p1, p2, p3, p4]
""" 
stock_value = 0

for p in products:
    print(f"id = {p["id"]}, name = {p["name"]}, cost = {p["cost"]}, units = {p["units"]}")
    product_value = p["cost"] * p["units"]
    stock_value += product_value 
print(f"Stock value : {stock_value}")
"""

# transform the product list into a list of product values
# product_value_list = [p["cost"] * p["units"] for p in products if p["in_stock"]]
unpacked_products = [ p.values() for p in products if p["in_stock"]]
product_value_list = [cost * units for id, name, cost, units, in_stock in unpacked_products]

# aggregate the product value list
stock_value = sum(product_value_list)

# transform the product list into a list of strings for printing
product_list_str = [f"id = {id}, name = {name}, cost = {cost}, units = {units}, in-stock = {in_stock}" for id, name, cost, units, in_stock in [ p.values() for p in products ] if in_stock]

# append the list of strings with a new line (\n)
product_list_output = "\n".join(product_list_str)

# print everything
print("In Stock products list:")
print(product_list_output)
print(f"Stock value (In Stock) : {stock_value}")

