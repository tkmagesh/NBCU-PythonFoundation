# Print all the prime numbers between 2 to 100
for no in range(2,101):
    x = int(no / 2)
    is_prime = True
    for i in range(2, x):
        if no % i == 0:
            is_prime = False
            break
    if is_prime:
        print(no)
