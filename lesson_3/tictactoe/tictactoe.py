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

GAMES_TO_WIN = 1

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


def simulate_move(board, move, marker):
    board[move] = marker
    winner = detect_winner(board)
    board[move] = INITIAL_MARKER
    return winner


def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return

    square = None

    for move in empty_squares(board):

        # offensive first
        if simulate_move(board, move, COMPUTER_MARKER):
            square = move
            break

    if not square:
        for move in empty_squares(board):

            # then defensive
            if simulate_move(board, move, HUMAN_MARKER):
                square = move
                break

    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER


def choose_square(board, current_player="Player"):
    if current_player == "Player":
        player_chooses_square(board)
    else:
        computer_chooses_square(board)


def alternate_player(current_player="Player"):
    return "Computer" if current_player == "Player" else "Player"


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
        current_player = "Player"

        prompt(f"First to {GAMES_TO_WIN} wins!")

        while player_wins < GAMES_TO_WIN and computer_wins < GAMES_TO_WIN:
            board = initialize_board()

            while True:

                display_board(board)

                choose_square(board, current_player)
                current_player = alternate_player(current_player)
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
        while True:
            answer = input().lower()

            if answer == "n" or answer == "y":
                break
            else:
                prompt("Please choose a valid option (y or n)")

        if answer == "n":
            break

    prompt("Thanks for playing Tic Tac Toe!")


play_tic_tac_toe()
