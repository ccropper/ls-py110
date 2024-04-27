import random
from utils import prompt

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

def deal_cards(deck, player):
    # need to grab 2 card from deck
    if player == 'human':
        player_hand.append(deck.pop())
        player_hand.append(deck.pop())
    elif player == 'computer':
        computer_hand.append(deck.pop())
        computer_hand.append(deck.pop())
    else:
        pass

# 1. Initialize deck

playing_deck = initialize_deck()

# 2. Deal cards to player and dealer

deal_cards(playing_deck, 'human')
deal_cards(playing_deck, 'computer')

print(player_hand)
print(computer_hand)

# 3. Player turn: hit or stay
#    - repeat until bust or stay
# 4. If player bust, dealer wins.
# 5. Dealer turn: hit or stay
#    - repeat until total >= 17
# 6. If dealer busts, player wins.
# 7. Compare cards and declare winner.