import random

""" 
Higher Order Functions
- functions can be treated like data
- assign function as value to a variable
- pass function as an argument to another function
- return function as a return value
"""

""" function as an argument """

def f1():
    print("f1 invoked")

def f2():
    print("f2 invoked")

def exec(fn):
    fn()

""" 
exec(f1)
exec(f2) 
"""

""" function as a return value """

def get_fn():
    no = random.randint(1,20)
    if no % 2 == 0:
        return f1
    else:
        return f2

fn = get_fn()
fn()

""" funtion as a value """

""" lambda with no arguments """
fx = lambda : print("fx invoked")
fx()

""" lambda with 1 argument """
is_odd = lambda no: False if no % 2 == 0 else True

print(is_odd(20))
print(is_odd(21))

""" lambda with 2 arguments """
add = lambda x,y: x + y
print(add(100,200))