""" Functions """
def fn():
    print("fn invoked!")

""" 
count - "parameter"
repeat_fn(count) - "signature of the function"
"""
def repeat_fn(count):
    for i in range(count):
        fn()

repeat_fn(2)
""" 
15 - "argument"
"""

def greet(name):
    print(f"Hello {name}, Have a nice day!")

greet("Magesh")

def repeat_greet(count, name):
    for i in range(count):
        greet(name)

repeat_greet(5, "Matt")

""" modify the above to allow customization of the "message" (Have a nice day!) as well!"""
