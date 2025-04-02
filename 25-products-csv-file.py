""" 
Using the "csv" package
Read the data from "products.csv" and print the list & stock value
"""

import csv

products = []

# Load the data from the file
with open("products.csv", 'r') as file:
    # create a dictionary reader
    reader = csv.DictReader(file, fieldnames=["id", "name", "cost", "units", "in_stock"])

    # read each row
    for row in reader:
        print(row)
        # convert each value into their respective type and create a product dictionary
        p = {
            "id" : int(row["id"]),
            "name" : row["name"],
            "cost" : float(row["cost"]),
            "units" : int(row["units"]),
            "in_stock" : bool(row["in_stock"])
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

# Write / Append new product
new_product = {
    "id" : 200,
    "name" : "Mouse",
    "cost" : 1200,
    "units" : 0,
    "in_stock" : False
}

with open("products.csv", 'a') as file:
    # create a dictionary writer
    writer = csv.DictWriter(file, fieldnames=["id", "name", "cost", "units", "in_stock"])
    writer.writerow(new_product)

print("new product added!")