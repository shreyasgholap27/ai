# 8-Queens Problem using Backtracking

N = 8

def print_board(board):
    """Print the chessboard with queens."""
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]."""

    # Check left side of current row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve_queens(board, col):
    """Solve the problem using backtracking."""

    # All queens placed
    if col >= N:
        return True

    # Try each row in current column
    for row in range(N):

        if is_safe(board, row, col):

            # Place queen
            board[row][col] = 1

            # Recur for next column
            if solve_queens(board, col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Driver Program
board = [[0 for _ in range(N)] for _ in range(N)]

if solve_queens(board, 0):
    print("Solution Found:\n")
    print_board(board)
else:
    print("No solution exists.")


    
'''
OUTPUT=
Solution Found:

Q . . . . . . .
. . . . . . Q .
. . . . Q . . .
. . . . . . . Q
. Q . . . . . .
. . . Q . . . .
. . . . . Q . .
. . Q . . . . .

'''
