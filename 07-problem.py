""" 
From the range 1 - 20
print the first five multiples of 3 
"""


multiples_count = 0
for no in range(1,21):
    if no % 3 == 0:
        multiples_count += 1
        print(no)
    if multiples_count == 5:
        break



