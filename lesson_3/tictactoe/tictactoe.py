"""

Display the initial empty 3x3 board.
Ask the user to mark a square.
Computer marks a square.
Display the updated board state.
If it's a winning board, display the winner.
If the board is full, display tie.
If neither player won and the board is not full, go to #2
Play again?
If yes, go to #1
Goodbye!

"""

import random
import os
from utils import join_or

INITIAL_MARKER = " "
HUMAN_MARKER = "X"
COMPUTER_MARKER = "O"

WINNING_LINES = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],  # rows
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],  # columns
    [1, 5, 9],
    [3, 5, 7],  # diagonals
]

GAMES_TO_WIN = 5


def prompt(message):
    print(f"=> {message}")


def display_board(board):
    os.system("clear")

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print("")
    print("     |     |")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print("     |     |")
    print("")


def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}


def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]


def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER


# computer randomly chooses square

# def computer_chooses_square(board):
#     if len(empty_squares(board)) == 0:
#         return
#     square = random.choice(empty_squares(board))
#     board[square] = COMPUTER_MARKER

# computer chooses square defensively

""" 
mini-PEDAC

### P ###

we want the computer to choose defensively

if 2 out of the 3 spaces out of a winning line is filled by a player marker, the computer should choose the 3rd spot
input: board state
output: the position corresponding to a key in the board state dict

### E ###

    if player has 1, 2, then computer should choose 3
    if player has 2, 3, then computer should choose 1
    if player has 1, 7, then computer should choose 4


### D ###

dictionary representing board state
list representing each of the winning lines 

### A ###

option 1:

when it's the computer's turn:
    make the board state available
    loop through winning lines and check if the player has 2 of them

    loop through winning lines list:

        make a new dict that uses the board state dict value corresponding to the position

        # e.g. [PLAYER_TOKEN, COMPUTER_TOKEN, INITIAL_MARKER]
        # e.g. [PLAYER_TOKEN, PLAYER_TOKEN, COMPUTER_TOKEN]
        # e.g. [PLAYER_TOKEN, PLAYER_TOKEN, INITIAL_MARKER]

        check the count of PLAYER_TOKEN in new dict values

        if count of PLAYER_TOKEN in new dict values is 2 and remaining square is empty:
            assign computer square to the key of the remaining square
        
    otherwise, return random square for computer choice


option 2:

when it's the computer's turn:
    make the board state available
    player_token_list
    loop through the player's positions. for each position:
        loop through each winning line that contains the player's position
            make a copy of winning_line
            remove the player's position from winning_line_evaluated
            loop through remaining spots in player_token_list:
                if player position in a winning line:
                    pop the number corresponding to the player position from winning_line_evaluated
                    check if it is an available spot. if so:
                        assign square = remaining number as computer position
    
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER   


option 3:

get all empty spots still available

for each empty spot:
    try to put the player marker there
        if then player wins, set computer choice to that square
    otherwise choose randomly amongst the empty squares
    return square

### C ###

see below for implementation of option 3    
"""


def computer_chooses_square(board, style="defensive"):
    if len(empty_squares(board)) == 0:
        return

    for square in empty_squares(board):

        # defensive

        simulated_board = board.copy()

        simulated_board[square] = HUMAN_MARKER

        simulated_winner = detect_winner(simulated_board)

        if simulated_winner == "Player":
            break

        # then offensive

        simulated_board = board.copy()

        simulated_board[square] = COMPUTER_MARKER

        simulated_winner = detect_winner(simulated_board)

        if simulated_winner == "Computer":
            break

    if not simulated_winner:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER


def board_full(board):
    return len(empty_squares(board)) == 0


def someone_won(board):
    return bool(detect_winner(board))


def detect_winner(board):

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (
            board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER
        ):
            return "Player"
        elif (
            board[sq1] == COMPUTER_MARKER
            and board[sq2] == COMPUTER_MARKER
            and board[sq3] == COMPUTER_MARKER
        ):
            return "Computer"

    return None


def play_tic_tac_toe():

    while True:
        player_wins = 0
        computer_wins = 0

        prompt(f"First to {GAMES_TO_WIN} wins!")

        while player_wins < GAMES_TO_WIN and computer_wins < GAMES_TO_WIN:
            board = initialize_board()

            while True:

                display_board(board)

                player_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

            display_board(board)

            if someone_won(board):
                winner = detect_winner(board)
                if winner == "Player":
                    player_wins += 1
                if winner == "Computer":
                    computer_wins += 1
                prompt(f"{winner} won!")
            else:
                prompt("It's a tie!")

            prompt(f"Player has {player_wins} wins. Computer has {computer_wins} wins.")
            input()

        if player_wins > computer_wins:
            prompt("Player won the match!")
        else:
            prompt("Computer won the match!")

        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer and answer[0] != "y":
            break

    prompt("Thanks for playing Tic Tac Toe!")


play_tic_tac_toe()
