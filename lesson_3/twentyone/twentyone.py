import os
import random
from utils import prompt

CARD_BACK = "\u2591"
SUITS = ("\u2663", "\u2665", "\u2666", "\u2660")
VALUES = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
GAMES_TO_WIN = 5


def make_card(card, hidden=False):
    card_display = ""
    if hidden:
        card_display += ".-------.\n"
        card_display += f"|{CARD_BACK*7}|\n"
        card_display += f"|{CARD_BACK*7}|\n"
        card_display += f"|{CARD_BACK*7}|\n"
        card_display += f"|{CARD_BACK*7}|\n"
        card_display += f"|{CARD_BACK*7}|\n"
        card_display += "`-------`\n"
    else:
        if card[0] != "10":
            card_display += ".-------.\n"
            card_display += f"| {card[0]}     |\n"
            card_display += "|       |\n"
            card_display += f"|   {card[1]}   |\n"
            card_display += "|       |\n"
            card_display += f"|     {card[0]} |\n"
            card_display += "`-------`"
        else:
            card_display += ".-------.\n"
            card_display += f"| {card[0]}    |\n"
            card_display += "|       |\n"
            card_display += f"|   {card[1]}   |\n"
            card_display += "|       |\n"
            card_display += f"|    {card[0]} |\n"
            card_display += "`-------`"

    return card_display


def display_hand(hand, sep="  ", is_dealer=False, conceal_card=False):

    if is_dealer:
        prompt("Dealer's hand: ")
    else:
        prompt("Your hand: ")

    if not conceal_card:
        cards = [make_card([card[1], card[0]]) for card in hand]
    else:
        cards = [make_card([card[1], card[0]]) for card in hand[:-1]]
        cards.append(make_card([hand[-1][0], hand[-1][1]], hidden=True))

    lines = [card.split("\n") for card in cards]

    for line_num in range(len(lines[0])):
        for card_line in lines:
            print(card_line[line_num], end="")
            print(sep, end="")
        print()


def create_deck():
    return [[suit, value] for suit in SUITS for value in VALUES]


def prompt_with_separator(msg, delimiter="-", width=60):
    print(f"{delimiter * width}")
    prompt(msg)


def player_turn(player_hand, playing_deck, total_to_win):
    while True:
        prompt_with_separator("Do you hit (h) or stay (s)?")
        while True:
            choice = input().strip()
            if choice in ("h", "s"):
                break
            prompt_with_separator("Please choose between hit (h) or stay (s).")

        if choice == "s":
            prompt_with_separator(
                f"You decide to stay. Your hand total is {total(player_hand, total_to_win)}."
            )
            break
        if choice == "h":
            prompt_with_separator("You decide to hit.")
            deal_card(player_hand, playing_deck)
            display_hand(player_hand)


def get_total_to_win():
    prompt("What should be the total point value to win the hand? (21 - 99)")
    while True:
        try:
            total_to_win = int(input())
            break
        except ValueError:
            prompt("Please enter an integer between 21 and 99. ")
    return total_to_win


def shuffle(cards):
    random.shuffle(cards)


def initialize_deck():
    deck = create_deck()
    shuffle(deck)
    return deck


def deal_card(hand, deck):
    hand.append(deck.pop())


def total(cards, total_to_win=21):
    # cards = [['H', '3'], ['S', 'Q'], ... ]
    values = [card[1] for card in cards]

    sum_val = 0
    for value in values:
        if value == "A":
            sum_val += 11
        elif value in ["J", "Q", "K"]:
            sum_val += 10
        else:
            sum_val += int(value)

    # correct for Aces
    aces = values.count("A")
    while sum_val > total_to_win and aces:
        sum_val -= 10
        aces -= 1

    return sum_val


def is_busted(hand, total_to_win=21):
    if total(hand) > total_to_win:
        return True
    return False


def dealer_turn(hand, deck, total_to_win=21):
    while total(hand, total_to_win) < total_to_win - 4:
        deal_card(hand, deck)
        prompt(
            f"Dealer hits! They are dealt a {hand[-1][1]} of {hand[-1][0]} from the deck..."
        )
    prompt_with_separator("Dealer stays.")


def play_again():
    prompt_with_separator("Play again? (y or n)")

    while True:
        answer = input().lower()

        if answer in ("n", "y"):
            break

        prompt_with_separator("Please choose a valid option (y or n)")

    if answer == "n":
        return False

    return True


def play_twentyone():

    while True:
        player_wins = 0
        computer_wins = 0

        prompt_with_separator("Welcome to Whatever-One.")

        total_to_win = get_total_to_win()

        while player_wins < GAMES_TO_WIN and computer_wins < GAMES_TO_WIN:

            os.system("clear")

            prompt_with_separator(f"Welcome to {total_to_win}.")
            prompt(f"First to win {GAMES_TO_WIN} games wins the match!")

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

            display_hand(computer_hand, is_dealer=True, conceal_card=True)

            while True:

                # 3. Player turn: hit or stay
                #    - repeat until bust or stay

                player_turn(player_hand, playing_deck, total_to_win)

                player_total = total(player_hand, total_to_win)

                # 4. If player bust, dealer wins.
                if is_busted(player_hand, total_to_win):
                    winner = "dealer"

                if winner:
                    prompt_with_separator("You busted!")
                    prompt_with_separator("The dealer wins!")
                    computer_wins += 1
                    break

                # 5. Dealer turn: hit or stay
                #    - repeat until total >= 17

                dealer_turn(computer_hand, playing_deck, total_to_win)

                computer_total = total(computer_hand, total_to_win)

                # reveal dealer hand

                display_hand(computer_hand, is_dealer=True, conceal_card=False)
                prompt(f"The dealer's hand total is {computer_total}.")

                # 6. If dealer busts, player wins.

                if is_busted(computer_hand, total_to_win):
                    prompt_with_separator("The dealer busted!")
                    prompt_with_separator("You win!")
                    player_wins += 1
                    break

                # 7. Compare cards and declare winner.

                if player_total > computer_total:
                    prompt_with_separator("You win!")
                    player_wins += 1
                    break
                if computer_total > player_total:
                    prompt_with_separator("Dealer wins!")
                    computer_wins += 1
                    break
                prompt_with_separator("It's a tie!")
                break

            prompt_with_separator(
                f"Player has {player_wins} wins. Computer has {computer_wins} wins."
            )
            prompt("Press enter to continue.")
            input()

        if player_wins > computer_wins:
            prompt("Player won the match!")
        else:
            prompt("Computer won the match!")

        if not play_again():
            break

        prompt_with_separator("Thanks for playing Whatever-One!")


play_twentyone()
