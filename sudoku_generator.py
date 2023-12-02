import math,random

class SudokuGenerator:

    def __init__(self, removed_cells, row_length=9):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for c in range(9)] for r in range(9)]
        self.box_length = math.sqrt(row_length)
    # row_length = the number of rows/columns of the board (always 9 for this project)
    # removed_cells = an integer value that contains the number of cells to be removed

    def get_board(self):
        return self.board

    def print_board(self):
        for r in range(9):
            for c in range(9):
                print(self.board[r][c], end="")
            print()

    def valid_in_row(self, row, num):
        pass
    # Determines if num is contained in the specified row (horizontal) of the board
    # If num is already in the specified row, return False. Otherwise, return True
    # row = the index of the row we are checking
    # num = the value we are looking for in the row
    # Return: boolean

    def valid_in_col(self, col, num):
        pass
    # Determines if num is contained in the specified column (vertical) of the board
    # If num is already in the specified col, return False. Otherwise, return True
    # col = the index of the column we are checking
    # num = the value we are looking for in the column
    # Return: boolean

    def valid_in_box(self, row_start, col_start, num):
        pass
    # Determines if num is contained in the 3x3 box specified on the board
    # If num is in the specified box starting at (row_start, col_start), return False.
    # Otherwise, return True
    # row_start, col_start = the starting indices of the box to check
    # 	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
    # num = the value we are looking for in the box
    # Return: boolean

    def is_valid(self, row, col, num):
        pass
    # Determines if it is valid to enter num at (row, col) in the board
    # This is done by checking that num is unused in the appropriate, row, column, and box
    # row, col = the row index and col index of the cell to check in the board
    # num = the value to test if it is safe to enter in this cell
    # Return: boolean

    def fill_box(self, row_start, col_start):
        pass
    # Fills the specified 3x3 box with values
    # For each position, generates a random digit which has not yet been used in the box
    # row_start, col_start = the starting indices of the box to check
    # 	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
    # Return: None

    def fill_diagonal(self):
        pass
    # Fills the three boxes along the main diagonal of the board
    # These are the boxes which start at (0,0), (3,3), and (6,6)
    # Parameters: None
    # Return: None

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
        # Fills the remaining cells of the board, should be called after the diagonal boxes have been filled
        # row, col = specify the coordinates of the first empty (0) cell

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
        # Constructs a solution by calling fill_diagonal and fill_remaining

    def remove_cells(self):
        pass
    # Removes the appropriate number of cells from the board
    # This is done by setting some values to 0
    # Should be called after the entire solution has been constructed
    #     i.e. after fill_values has been called
    # NOTE: Be careful not to 'remove' the same cell multiple times
    #     i.e. if a cell is already 0, it cannot be removed again
    # Parameters: None
    # Return: None

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
    # Creates a SudokuGenerator, fills its values and saves this as the solved state,
    # removes the appropriate number of cells, and returns the representative 2D python lists of board/solution
    # size = number of rows/columns of the board
    # removed = number of cells to clear (set to 0)
