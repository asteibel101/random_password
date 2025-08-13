import random

def get_int_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Please enter a valid number.")

# Character pools
letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

print("Welcome to the PyPassword Generator!")

# User input
nr_letters = get_int_input("How many letters would you like in your password? ")
nr_symbols = get_int_input("How many symbols would you like? ")
nr_numbers = get_int_input("How many numbers would you like? ")

# Build password components
password_list = []

# Add letters
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add symbols
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add numbers
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the list
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

print(f"\nYour generated password is: {password}")
