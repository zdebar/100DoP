#Step 1 

import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess the letter: ").lower()
word_guess = ["_"]*len(chosen_word)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

position = 0
for letter in chosen_word:
    if letter == guess:
        print("Right")
        word_guess[position] = letter
    else:
        print("Wrong")
    position += 1

print(word_guess)