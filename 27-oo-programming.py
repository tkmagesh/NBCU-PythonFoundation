
# blueprint for a Product object
class Product:

    # __init__() method is automatically executed whenever an instance of the class is created
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

    # 
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

p = Product(100, "Pen", 5.99, 10)
# print(p.id, p.name, p.cost, p.units)
# print(f"id={p.id}, name={p.name}, cost={p.cost}, units={p.units}")
# print(p.string())
print(p)
print(f"Stock value of p : {p.get_stock_value()}")
# Ask to instance to exhibit a behavior
# p.who_am_i()