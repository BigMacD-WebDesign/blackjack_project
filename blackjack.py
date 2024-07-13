import random
from modules.art import logo
import os

clear = lambda: os.system('clear')

def deal_card():
    """Returns random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the card."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "Bust. You went over. You lose."
    elif computer_score > 21:
        return "You win! Dealer busts!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    #First while loop to calculate user score and allow user you continue getting more cards if requested.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            continue_game = input("Would you like to draw another card? Type 'y' or 'n'.")
            if continue_game == "y":
                user_cards.append(deal_card())
                calculate_score(user_cards)
            else:
                is_game_over = True
    
    # Second while loop to calculate Dealer's (computer) score:
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f" Your final hand is: {user_cards}, final score: {user_score}")
    print(f" Dealer's final hand is: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
# While loop to contine/begin game.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    print(logo)
    play_game()