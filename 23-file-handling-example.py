
def write_file():
    with open('data.dat', 'w') as file:
        file.write("Magna qui aliqua quis nostrud culpa reprehenderit pariatur pariatur culpa.\n")
        file.write("Aute et labore nulla ut nisi dolor excepteur nostrud proident incididunt est nostrud.\n")
        file.write("Consectetur adipisicing pariatur amet consectetur aliqua ut culpa aliqua duis fugiat do excepteur dolor dolor.\n")
    print("file created and data written!")

# write_file()

def read_file_by_line():
    with open('data.dat', 'r') as file:
        for line in file:
            print(f"line : {line}")
    print("That's all folks!")

read_file_by_line()

def append_file():
    with open('data.dat', 'a') as file:
        file.write("Cillum eu irure et excepteur.\n")
    print("New data appened")

# append_file()

