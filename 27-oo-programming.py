
# blueprint for a Product object
class Product:

    # __init__() method (dunder method) is automatically executed whenever an instance of the class is created
    def __init__(self, id, name, cost, units):
        # initialize the state (properties / attributes)
        self.id = id
        self.name = name
        self.cost = cost
        self.units = units
        print("A new product object is created")

    # method (behavior)
    def who_am_i(self):
        print("I am a product!")

    # automatically called when passed to the print() function
    def __str__(self):
        return f"id={self.id}, name={self.name}, cost={self.cost}, units={self.units}"
    
    def get_stock_value(self):
        return self.cost * self.units

# create an instance (object) using the blueprint (class)
""" 
p = Product()
# print(type(p))
p.id = 100
p.name = "Pen"
p.cost = 5.99
p.units = 20 
"""

""" 
p = Product(100, "Pen", 5.99, 10)
# print(p.id, p.name, p.cost, p.units)
# print(f"id={p.id}, name={p.name}, cost={p.cost}, units={p.units}")
# print(p.string())
print(p)
print(f"Stock value of p : {p.get_stock_value()}")
# Ask to instance to exhibit a behavior
# p.who_am_i() 
"""

class LineItem:
    def __init__(self, product, units, discount_percentage = 0):
        self.product = product
        self.units = units
        self.discount_percentage = discount_percentage

    def get_item_value(self):
        return (self.product.cost * self.units) * ((100 - self.discount_percentage)/100)

    def __str__(self):
        return f"id={self.product.id}, name={self.product.name}, cost={self.product.cost}, units ordered={self.units}, discount={self.discount_percentage}%"
    
""" 
class ShoppingCart:
    def __init__(self):
        self.line_items = []

    def add_product(self, product, units):
        self.line_items.append({ "product" : product, "units" : units})

    def get_total(self):
        total = 0
        for line_item in self.line_items:
            total += line_item["units"] * line_item["product"].cost
        return total

cart = ShoppingCart()
cart.add_product(p1, 5)
cart.add_product(p2, 10)
cart.add_product(p3, 7)
print(cart.get_total())
 """

#  Shopping Cart with line items
class ShoppingCart:
    def __init__(self):
        self.line_items = []

    def add_line_item(self, line_item):
        self.line_items.append(line_item)

    def get_total(self):
        total = 0
        for line_item in self.line_items:
            total += line_item.get_item_value()
        return total

    def __str__(self):
        return "\n".join([f"{line_item}" for line_item in self.line_items])


p1 = Product(101, "Pen", 5.99, 100)
p2 = Product(102, "Pencil", 2.99, 500)
p3 = Product(103, "Marker", 50.88, 50)

cart = ShoppingCart()
cart.add_line_item(LineItem(p1, 5, 10))
cart.add_line_item(LineItem(p2, 10, 5))
cart.add_line_item(LineItem(p3, 7, 7))
print(cart)
print(cart.get_total())