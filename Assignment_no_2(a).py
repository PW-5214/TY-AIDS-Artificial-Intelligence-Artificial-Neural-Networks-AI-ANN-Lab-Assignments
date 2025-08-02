def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True
    
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  
                return False  
    return True  

def print_grid(grid):
    for row in range(9):
        for col in range(9):
            print(grid[row][col], end=" ")
        print()

sudoku_grid = []
print("Enter the Sudoku grid row by row (use 0 for empty cells):")
i = 0
while i < 9:
    print("Row", i + 1, ": ", end="")
    row_input = input()
    row = []
    j = 0
    start = 0
    while j < len(row_input):
        if row_input[j] == ' ':
            row.append(int(row_input[start:j]))
            start = j + 1
        j += 1
    row.append(int(row_input[start:]))
    sudoku_grid.append(row)
    i += 1

if solve_sudoku(sudoku_grid):
    print("Sudoku Solved:")
    print_grid(sudoku_grid)
else:
    print("No solution exists for the given Sudoku.")
