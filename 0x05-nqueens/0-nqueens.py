import sys

def is_safe(board, row, col, N):
    # Check if the current position is attacked by any previously placed queens
    # Check the row and column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []

    def place_queen(col):
        if col == N:
            # Found a solution, convert the board to the desired format
            solution = [''.join('Q' if board[i][j] == 1 else '.' for j in range(N)) for i in range(N)]
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                # Place the queen and move to the next column
                board[row][col] = 1
                place_queen(col + 1)
                # Backtrack: remove the queen from the current position
                board[row][col] = 0

    place_queen(0)
    return solutions

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == '__main__':
    main()

