#!/usr/bin/python3
import sys


def print_solution(board):
    """Prints the board in the required format"""
    print([[row, col] for row, col in enumerate(board)])


def is_safe(board, row, col):
    """Checks if a queen can be placed on board[row][col]"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row=0, board=[]):
    """Backtracking solution to the N Queens problem"""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            solve_nqueens(n, row + 1, board + [col])


def main():
    """Main entry point: parses arguments and starts solving"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
