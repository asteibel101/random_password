import string
import secrets

def get_int_input(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)            # non-negative integer
        print("Please enter a valid number (0 or greater).")

# Character pools 
LETTERS = string.ascii_letters          # a-zA-Z
DIGITS  = string.digits                 # 0-9
SYMBOLS = "!#$%&()*+"

print("Welcome to the PyPassword Generator!")

# User input
nr_letters = get_int_input("How many letters would you like in your password? ")
nr_symbols = get_int_input("How many symbols would you like? ")
nr_numbers = get_int_input("How many numbers would you like? ")

# Define pools and their counts
char_pools = [
    (LETTERS, nr_letters),
    (SYMBOLS, nr_symbols),
    (DIGITS, nr_numbers)
]

# Build password list (secure choice) and shuffle securely
rng = secrets.SystemRandom()
password_list = [rng.choice(pool) for pool, count in char_pools for _ in range(count)]
rng.shuffle(password_list)

# Convert list to string
password = "".join(password_list)
print(f"\nYour generated password is: {password}")
