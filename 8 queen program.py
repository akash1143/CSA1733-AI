def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_queens(board, col, solutions):
    if col >= len(board):
        solutions.append([row[:] for row in board])
        return
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_queens(board, col + 1, solutions)
            board[i][col] = 0

def print_board(board):
    for row in board:
        print(" ".join('Q' if x == 1 else '.' for x in row))
    print()

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_queens(board, 0, solutions)
    print(f"Total solutions: {len(solutions)}")
    for solution in solutions:
        print_board(solution)

# Setting up an 8x8 board
solve_n_queens(8)
