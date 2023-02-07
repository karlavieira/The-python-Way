import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+','!', '#', '$', '%', '&', '*', '+','!', '#', '$', '%', '&', '*', '+']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

nr_numbers = int(input("How many numbers would you like in your password?\n"))

password = ""

for i in range(nr_letters):
    i = int(random.randint(0, len(letters) + 1))
    letter = letters[i]
    password = password + letter


for i in range(nr_numbers):
    i = int(random.randint(0, len(numbers)))
    number = numbers[i]
    password = password + number
    

for i in range(nr_symbols):
    i = int(random.randint(0, len(symbols) + 1))
    symbol = symbols[i]
    password = password + symbol

print(password)
perfect_password = (random.choice(password))
print(f"Your perfect password is {perfect_password}")