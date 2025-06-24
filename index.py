import random

# Character pools
letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

print("Welcome to the PyPassword Generator!")

# User input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

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
