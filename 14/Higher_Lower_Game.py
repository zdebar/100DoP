import game_data
import game_art
import random


def get_random_data():
    return random.choice(game_data.data)


def print_compare(D):
    return f"Compare A: {D["name"]}, {D["description"]}, {D["country"]}"


def evaluate(A, B, score):
    end_game = False
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if A['follower_count'] > B['follower_count']: 
            right_answer = "A"
    else:
        right_answer = "B"
    if guess == right_answer:
        score += 1
        print("Right!")
    else:
        end_game = True
        print("Wrong!")
    return end_game, score


def game():
    end_game = False
    score = 0
    while end_game == False:
        A = get_random_data()
        print(print_compare(A))

        print(game_art.vs)

        while True:
            B = get_random_data()
            if B != A:
                break
        print(print_compare(B))     
        
        end_game, score = evaluate(A, B, score)
        print(f"Your score is {score}!")
    return score


print(game_art.logo)
game()    




