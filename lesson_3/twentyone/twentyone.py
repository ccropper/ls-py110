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

def shuffle(cards):
    random.shuffle(cards)

def initialize_deck():
    playing_deck = COMPLETE_DECK
    shuffle(playing_deck)
    return playing_deck

def deal_card(hand, deck):
    # need to grab 2 card from deck
    hand.append(deck.pop())

def display_hand(hand, is_dealer = False):
    # if not is_dealer:
    #     str = "You are holding: "
    #     for card in range(0, len(hand)):
    #         str += f"{hand[card][1]} of {player_hand[card][0]}"
    # prompt(str)
    if not is_dealer:
        legible_hand = [f"{card[1]} of {card[0]}"  for card in hand]
        joined_hand = join_or(legible_hand, last_joining_word='and')
        prompt(f"Your hand: {joined_hand}.")
    else:
        legible_hand = [f"{card[1]} of {card[0]}"  for card in hand[:-1]]
        joined_hand = join_or(legible_hand, last_joining_word='and')
        prompt(f"Dealer's hand: {joined_hand} and a mystery card.")

def is_busted(hand):
    # check if hand is busted
    pass

# 1. Initialize deck

playing_deck = initialize_deck()

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

display_hand(computer_hand, is_dealer = True)

# 3. Player turn: hit or stay

while True:
    prompt("Do you hit (h) or stay (s)?")
    while True:
        choice = input().strip()
        if choice in ('h', 's'):
            break
        prompt("Please choose between hit (h) or stay (s).")

    if choice == 's':
        prompt("You decide to stay.")
        break
    if choice == 'h':
        deal_card(player_hand, playing_deck)
        display_hand(player_hand)
        if is_busted(player_hand):
            break


#    - repeat until bust or stay
# 4. If player bust, dealer wins.
# 5. Dealer turn: hit or stay
#    - repeat until total >= 17
# 6. If dealer busts, player wins.
# 7. Compare cards and declare winner.