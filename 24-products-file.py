""" 
Read the data from "products.csv" and print the list & stock value
"""

products = []

# Load the data from the file
with open("products.csv", 'r') as file:
    # read each line
    for line in file:
        # split the line by ","
        values = line.split(",")
        # convert each value into their respective type and create a product dictionary
        p = {
            "id" : int(values[0]),
            "name" : values[1],
            "cost" : float(values[2]),
            "units" : int(values[3]),
            "in_stock" : bool(values[4])
        }
        # append the product to the products list
        products.append(p)

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