#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N):
    if col >= N:
        # All queens are placed, print the solution
        solution = [[i, board[i].index(1)] for i in range(N)]
        print(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens_util(board, col + 1, N)

            '''
            Backtrack if placing the queen in the current position doesn't
            lead to a solution
            '''
            board[i][col] = 0


def solve_nqueens(N):
    # Initialize the chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Start with the first column
    solve_nqueens_util(board, 0, N)


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
