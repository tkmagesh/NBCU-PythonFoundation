""" 
maintain a collection of products
product attributes
    id
    name
    cost
    units
Print the products
Calculate the over all stock value and print it
    sum(cost * units)
"""

p1 = (101, "Pen", 5, 20)
p2 = (102, "Pencil", 2, 50)
p3 = (103, "Marker", 50, 10)
p4 = (104, "Scribble-Pad", 30, 25)

""" 
products = []
products.append(p1)
products.append(p2)
products.append(p3)
products.append(p4) 
"""

products = [p1, p2, p3, p4]

stock_value = 0

for p in products:
    # print(f"id = {p[0]}, name = {p[1]}, cost = {p[2]}, units = {p[3]}")
    id, name, cost, units = p # unpacking
    print(f"id = {id}, name = {name}, cost = {cost}, units = {units}")
    product_value = cost * units
    stock_value += product_value

print(f"Stock value : {stock_value}")