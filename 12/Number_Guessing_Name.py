# Classical Number Guessing Game
from random import randint
import os
os.system('cls' if os.name == 'nt' else 'clear')

logo = """
   _____                       _   _                 _                
  / ____|                     | \ | |               | |               
 | |  __ _   _  ___  ___ ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  
 | | |_ | | | |/ _ \/ __/ __| | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| 
 | |__| | |_| |  __/\__ \__ \ | |\  | |_| | | | | | | |_) |  __/ |    
  \_____|\__,_|\___||___/___/ |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    
""" 
def guess():
    count = 0
    number = randint(1,100)
    while True:  
        guess = int(input("Make a guess: "))
        count += 1
        if guess == number: 
            print(f"That's it. You needed {count} attempts!")
            break
        elif guess > number:
            print(  "Too high!")
        else:
            print(  "Too low!")    
        print(f"Number of guesses: {count}")
                                                                      
def game():
    print("Welcome to the Number Guessing Game!\n")
    print(logo)
    print("I'm thinking of a number between 1 and 100.") 
    guess()

game()

