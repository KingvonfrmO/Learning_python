import sys

def print_solution(solution):
    print([[i, row] for i, row in enumerate(solution)])

def is_safe(solution, row, col):
    for i in range(col):
        if (
            solution[i] == row or  # Same row
            abs(solution[i] - row) == abs(i - col)  # Same diagonal
        ):
            return False
    return True

def solve_nqueens(n, col=0, solution=[]):
    if col == n:
        print_solution(solution)
        return

    for row in range(n):
        if is_safe(solution, row, col):
            solve_nqueens(n, col + 1, solution + [row])

def main():
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
