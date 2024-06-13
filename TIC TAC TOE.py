def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Let's play Tic Tac Toe!")
    print_board(board)

    for _ in range(9):
        row = int(input(f"Player {players[current_player]}, enter row number (0-2): "))
        col = int(input(f"Player {players[current_player]}, enter column number (0-2): "))

        while board[row][col] != ' ':
            print("That position is already taken. Try again.")
            row = int(input(f"Player {players[current_player]}, enter row number (0-2): "))
            col = int(input(f"Player {players[current_player]}, enter column number (0-2): "))

        board[row][col] = players[current_player]
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            return

        current_player = (current_player + 1) % 2

    print("It's a draw!")

# Start the game
tic_tac_toe()
