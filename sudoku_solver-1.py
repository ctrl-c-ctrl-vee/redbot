def is_valid(board, row, col, num):
    # Check if `num` is not already placed in current row, current column and current 3x3 box
    for x in range(9):
        if board[row][x] == num:
            return False
        if board[x][col] == num:
            return False
    
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    empty_cell = find_empty_location(board)
    if not empty_cell:
        return True  # Puzzle solved
    
    row, col = empty_cell
    
    for num in range(1, 10):  # Try numbers from 1 to 9
        if is_valid(board, row, col, str(num)):
            board[row][col] = str(num)
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = "."  # Backtrack
    
    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                return (i, j)
    return None

# Example Sudoku puzzle
puzzle = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", "3", "4"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# Solve the puzzle
if solve_sudoku(puzzle):
    for row in puzzle:
        print(" ".join(row))
else:
    print("No solution exists")

