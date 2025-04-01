""" Functions """

""" With No arguments """
def fn():
    print("fn invoked!")


""" With 1 parameter """
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

""" 
def greet(name):
    print(f"Hello {name}, Have a nice day!")

greet("Magesh")

def repeat_greet(count, name):
    for i in range(count):
        greet(name)

repeat_greet(5, "Matt") 
"""

""" modify the above to allow customization of the "message" (Have a nice day!) as well!"""

""" With > 1 parameters """
def greet(name, msg):
    print(f"Hello {name}, {msg}")

# greet()
greet("Magesh", "Have a good day!")

def repeat_greet(count, name, msg):
    for i in range(count):
        greet(name, msg)

repeat_greet(5, "Matt", "Good day!")

""" With no parameter and 1 return result """
def get_pi():
    return 3.14

print(get_pi())

""" With parameter(s) and return result """
def greet_user(first_name, last_name):
    return f"Hi {first_name} {last_name}, Have a nice day!"

msg = greet_user("Magesh", "Kuppan")
print(msg)

""" With parameter(s) and > 1 return result """
def get_names(full_name): # full_name = "lastname, firstname"
    names = full_name.split(",")
    last_name = names[0].strip()
    first_name = names[1].strip()
    return first_name, last_name

""" 
x = get_names("Kuppan, Magesh")
print(x)
print(type(x)) 
"""

fn, ln = get_names("Kuppan, Magesh")
print(f"first name : {fn}")
print(f"last name : {ln}") 


""" With default arguments """
def greet_v2(name = "Guest", msg = "Good day!"):
    print(f"Hello {name}, {msg}")

greet_v2()
greet_v2("Magesh")
greet_v2("Matt", "Have a nice day!")

""" With Keyword arguments """
greet_v2(name = "Justyn", msg = "Have a wonderful day!")

""" order of arguments does not matter when keyword (parameter names) are used """
greet_v2(msg="Time for lunch!", name="Ashley")

