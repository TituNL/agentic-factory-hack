import random
from collections import Counter

player1_board = [[5, 5, 6], [3, 3, 1], [4, 4, None], ]
player2_board = [[1, 2, 3], [4, 4, 6], [None, None, None], ]

#player1_board = [[None, None, None], [None, None, None], [None, None, None], ]
#player2_board = [[None, None, None], [None, None, None], [None, None, None], ]

def print_board():
    print("1.",player1_board[0], "|", player2_board[0])
    print("2.",player1_board[1], "|", player2_board[1])
    print("3.",player1_board[2], "|", player2_board[2])


def rolling_dice() -> int:
    number1_6 = random.randint(1, 6)
    print(f"\nYou rolled {number1_6}!")

    return number1_6


def add_roll(roll_dice: int, current_board: list, opponent_board: list):
    while True:
        user_row_choice = input(f"Please enter a row to add {roll_dice} (1-3): ")

        try:
            user_row_choice = int(user_row_choice) - 1
        except ValueError:
            print(f"Please enter a valid row (1-3) to add {roll_dice}!")
            continue

        if user_row_choice not in range(3):
            print(f"Please enter a valid row (1-3) to add {roll_dice}!")
            continue

        selected_row = current_board[user_row_choice]
        opponent_row = opponent_board[user_row_choice]

        if None not in selected_row:
            print("This row is full. Choose another one!")
            continue

        for player_index in range(len(selected_row)):
            if selected_row[player_index] is None:
                selected_row[player_index] = roll_dice
                break

        for opponent_index in range(len(opponent_row)):
            if opponent_row[opponent_index] == roll_dice:
                opponent_row[opponent_index] = None

        break


def board_full_check(board):
    for row in board:
        for number in row:
            if number is None:
                return False

    return True


def calculate_points(board):
    total_score = 0
    for row in board:
        values_in_row = [value for value in row if value is not None]
        counts = Counter(values_in_row)

        for value, count in counts.items():
            total_score += value * count * count

    return total_score


def print_score(player_1_score, player_2_score):
    print(f"\nTotal score player 1: {player_1_score}")
    print(f"Total score player 2: {player_2_score}")

    if player_1_score > player_2_score:
        print("Player 1 wins!")
    elif player_2_score > player_1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")


def main():
    current_player = 1
    round_number = 1
    while True:
        print(f"\n ----- Round {round_number} -----")
        print(f"It's player {current_player}'s turn!")
        print_board()
        roll_dice = rolling_dice()

        if current_player == 1:
            add_roll(roll_dice, player1_board, player2_board)
        else:
            add_roll(roll_dice, player2_board, player1_board)

        if current_player == 1:
            current_player = 2
        else:
            current_player = 1

        round_number += 1

        if board_full_check(player1_board) or board_full_check(player2_board):
            break

    print("\nGame finished!")
    print_board()

    player_1_score = calculate_points(player1_board)
    player_2_score = calculate_points(player2_board)
    print_score(player_1_score, player_2_score)


if __name__ == "__main__":
    main()
