#Password Generator Project
from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def check_value_error(message):
    while True:
        try:
            a = int(input(f"{message}\n")) 
            break
        except ValueError:
            print("Has to be integer!\n")
    return a

print("Welcome to the PyPassword Generator!")
nr_letters = check_value_error("How many letters would you like in your password?")
nr_symbols = check_value_error("How many symbols would you like?")
nr_numbers = check_value_error("How many numbers would you like?")

#Hard Level - Order of characters randomised:

pass_list = [choice(letters) for _ in range(nr_letters)] + [choice(numbers) for _ in range(nr_symbols)] + [choice(symbols) for _ in range(nr_numbers)]
shuffle(pass_list)
password = "".join(pass_list)
print(f"Your password is: {password}")
    
