def display_board(board):
    i = 0
    print("\nTIC TAC TOE")
    print("*" * 20)
    for row in board:
        print("*", "   | ".join(row), "   *")
        i += 1
        if i != len(board):
            print("*", "-" * 3, "|", "-" * 3, "|", "-" * 3, " *")
    print("*" * 20)

def player_input(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

def check_win(board):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],  # Rows
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],  # Columns
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],  # Diagonals
        [(0, 2), (1, 1), (2, 0)]
    ]
    for combo in winning_combinations:
        if board[combo[0][0]][combo[0][1]] == board[combo[1][0]][combo[1][1]] == board[combo[2][0]][combo[2][1]] != " ":
            return board[combo[0][0]][combo[0][1]]
    return None

def play():
    print("Welcome to TIC TAC TOE!")
    board = [[" "] * 3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for _ in range(9):
        display_board(board)
        player_input(players[turn], board)
        winner = check_win(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            return
        turn = 1 - turn 
    
    display_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    play()
