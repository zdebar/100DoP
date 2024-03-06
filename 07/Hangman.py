#Step 1 

import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

letter_guess = ["_"]*len(chosen_word)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

lives = 6

while "_" in (letter_guess):
    position = 0
   
    guess = input("Guess the letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            letter_guess[position] = letter
        else:
            position += 1
    if guess not in chosen_word:
        lives -= 1
    print(f"You have {lives} lives.")
    if lives == 0:
        print("You lose")
        break

    
    print("".join(letter_guess))

