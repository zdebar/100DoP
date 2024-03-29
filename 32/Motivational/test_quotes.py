import random

quotes_file = "32/Motivational/quotes.txt"

with open("32/Motivational/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

for quote in all_quotes:
    print(quote)