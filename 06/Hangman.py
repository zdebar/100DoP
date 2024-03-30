import random

lives = 6
import_words = "kohoutek | těstoviny | návštěvník | čelo | vědec | časoprostor | kostlivec | boj | legrace | úlet"
words = import_words.split(" | ")


selected_word = random.choice(words)
guess_word = ["_"]*len(selected_word)


while lives and not guess_word == selected_word:
    print(f"Počet životů {lives}, slovo {" ".join(guess_word)}")
    guess = input("Hádej písmeno: ").lower()
    found = False
    for index in range(len(selected_word)):
        if guess == selected_word[index]:
            guess_word[index] = guess
            found = True
    if not found: 
        lives -= 1

print(f"Správné slovo bylo '{"".join(selected_word)}'!", end=" " )
if guess_word == selected_word:
    print("Vyhrál jsi!")
else:
    print("Prohrál jsi!")

    

#     break
    

