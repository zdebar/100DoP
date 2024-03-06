import random
import os

print("Welcome to simplified black jack games")

def deal_card(cards_drawn):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choices(cards,k=cards_drawn)
    return card

def calculate_score(cards):
    """ Takes a list of cards and calculate score"""
    if sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)   

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    user_cards += deal_card(2)
    computer_cards += deal_card(2)

    while is_game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards:            {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
                user_cards += deal_card(1)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards += deal_card(1)
        computer_score = calculate_score(computer_cards)

    print(f"    Your cards:            {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards}, computer's score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do yout want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()

# print(f"Your cards:    {player_hand}, Value sum: {player_sum}")
# print(f"Computer card: {computer_hand}")


