import os
import random
from utils import prompt, join_or

COMPLETE_DECK = [
    ["Hearts", "A"], ["Diamonds", "A"], ["Clubs", "A"], ["Spades", "A"],
    ["Hearts", "2"], ["Diamonds", "2"], ["Clubs", "2"], ["Spades", "2"],
    ["Hearts", "3"], ["Diamonds", "3"], ["Clubs", "3"], ["Spades", "3"],
    ["Hearts", "4"], ["Diamonds", "4"], ["Clubs", "4"], ["Spades", "4"],
    ["Hearts", "5"], ["Diamonds", "5"], ["Clubs", "5"], ["Spades", "5"],
    ["Hearts", "6"], ["Diamonds", "6"], ["Clubs", "6"], ["Spades", "6"],
    ["Hearts", "7"], ["Diamonds", "7"], ["Clubs", "7"], ["Spades", "7"],
    ["Hearts", "8"], ["Diamonds", "8"], ["Clubs", "8"], ["Spades", "8"],
    ["Hearts", "9"], ["Diamonds", "9"], ["Clubs", "9"], ["Spades", "9"],
    ["Hearts", "10"], ["Diamonds", "10"], ["Clubs", "10"], ["Spades", "10"],
    ["Hearts", "J"], ["Diamonds", "J"], ["Clubs", "J"], ["Spades", "J"],
    ["Hearts", "Q"], ["Diamonds", "Q"], ["Clubs", "Q"], ["Spades", "Q"],
    ["Hearts", "K"], ["Diamonds", "K"], ["Clubs", "K"], ["Spades", "K"]
]

player_hand = []
computer_hand = []

def prompt_with_separator(msg):
    print(f"{'~' * 60}")
    prompt(msg)

def shuffle(cards):
    random.shuffle(cards)

def initialize_deck():
    os.system("clear")
    playing_deck = COMPLETE_DECK
    shuffle(playing_deck)
    return playing_deck

def deal_card(hand, deck):
    # need to grab 2 card from deck
    hand.append(deck.pop())

def display_hand(hand, is_dealer = False, conceal_card = False):
    msg = ""
    if is_dealer:
        msg += "Dealer's hand: "
    if not is_dealer:
        msg += "Your hand: "
    if not conceal_card:
        legible_hand = [f"{card[1]} of {card[0]}"  for card in hand]
        joined_hand = join_or(legible_hand, last_joining_word='and')
        msg += f"{joined_hand}."
    else:
        legible_hand = [f"{card[1]} of {card[0]}"  for card in hand[:-1]]
        joined_hand = join_or(legible_hand, last_joining_word='and')
        msg += f"{joined_hand} and a secret card."

    prompt(msg)

def total(cards):
    # cards = [['H', '3'], ['S', 'Q'], ... ]
    values = [card[1] for card in cards]

    sum_val = 0
    for value in values:
        if value == "A":
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    # correct for Aces
    aces = values.count("A")
    while sum_val > 21 and aces:
        sum_val -= 10
        aces -= 1

    return sum_val

def is_busted(hand):
    if total(hand) > 21:
        return True
    else:
        return False
    
def dealer_turn(hand, deck):
    while total(hand) < 17:
        deal_card(hand, deck)
        prompt(f"Dealer is dealt a {hand[-1][1]} of {hand[-1][0]} from the deck...")
    pass


while True:

    prompt_with_separator("Welcome to Twenty-one.")

    # 1. Initialize deck

    playing_deck = initialize_deck()
    winner = None

    # 2. Deal cards to player and dealer

    player_hand = []
    computer_hand = []

    deal_card(player_hand, playing_deck)
    deal_card(player_hand, playing_deck)
    deal_card(computer_hand, playing_deck)
    deal_card(computer_hand, playing_deck)

    # display your hand

    display_hand(player_hand)

    # display one card from computer's hand

    display_hand(computer_hand, is_dealer = True, conceal_card=True)

    while True:

        # 3. Player turn: hit or stay
        #    - repeat until bust or stay

        while True:
            prompt_with_separator("Do you hit (h) or stay (s)?")
            while True:
                choice = input().strip()
                if choice in ('h', 's'):
                    break
                prompt_with_separator("Please choose between hit (h) or stay (s).")

            if choice == 's':
                prompt_with_separator("You decide to stay.")
                break
            if choice == 'h':
                deal_card(player_hand, playing_deck)
                display_hand(player_hand)
                if is_busted(player_hand):
                    winner = 'dealer'
                    break

    # 4. If player bust, dealer wins.

        if winner:
            prompt_with_separator("You busted!")
            prompt_with_separator("Dealer wins!")
            break

        # 5. Dealer turn: hit or stay
        #    - repeat until total >= 17

        dealer_turn(computer_hand, playing_deck)

        # reveal dealer hand

        display_hand(computer_hand, is_dealer=True, conceal_card=False)

        # 6. If dealer busts, player wins.

        if is_busted(computer_hand):
            prompt_with_separator("You win!")
            break

        # 7. Compare cards and declare winner.


        if total(player_hand) > total(computer_hand):
            prompt_with_separator("You win!")
            break
        if total(computer_hand) > total(player_hand):
            prompt_with_separator("Dealer wins!")
            break
        else:
            prompt_with_separator("It's a tie!")
            break
    
    prompt_with_separator("Play again? (y or n)")

    while True:
        answer = input().lower()

        if answer == "n" or answer == "y":
            break
        else:
            prompt_with_separator("Please choose a valid option (y or n)")

    if answer == "n":
        break

    prompt_with_separator("Thanks for playing Twenty-One!")






