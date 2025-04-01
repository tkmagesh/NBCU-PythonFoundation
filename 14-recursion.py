
count = 0

def fn():
    global count
    print(count)
    print("fn invoked")
    count = count + 1
    if count > 10:
        return
    fn()

fn()

""" factorial(5) = 1 * 2 * 3 * 4 * 5 = 120 """

def factorial(no):
    result = 1
    for i in range(1,no+1):
        result *= i
    return result

print(factorial(5))

def factorial_recursion(no):
    if no == 0:
        return 1
    return no * factorial_recursion(no - 1)

print(factorial_recursion(5))