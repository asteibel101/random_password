# PyPassword Generator

A simple Python program to generate strong, random passwords based on user preferences for letters, symbols, and numbers.

## Features

- Lets you choose the number of **letters**, **symbols**, and **numbers** in your password.
- Randomly selects characters from predefined character pools.
- Shuffles characters for extra randomness.
- Outputs a secure, mixed-character password.

## How It Works

1. **Character Pools:**

   - **Letters:** Uppercase and lowercase English letters (`a-z`, `A-Z`).
   - **Numbers:** Digits `0-9`.
   - **Symbols:** `!#$%&()*+`.

2. **User Input:**

   - Prompts you for how many letters, symbols, and numbers to include.

3. **Password Generation:**

   - Randomly picks characters from each pool based on your choices.
   - Combines all selected characters into a list.
   - Shuffles the list for randomness.
   - Joins them into a single string to create the password.

4. **Output:**
   - Displays your generated password in the terminal.

## Usage

1. Save the code as `pypassword_generator.py`.
2. Run it using:
   ```bash
   python pypassword_generator.py
   ```
