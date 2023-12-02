import math
from random import randint

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
        for r in self.board[row]:
            if r == num:
                return False
        return True
    # Determines if num is contained in the specified row (horizontal) of the board

    def valid_in_col(self, col, num):
        for r in range(9):
            if self.board[r][col] == num:
                return False
        return True
    # Determines if num is contained in the specified column (vertical) of the board

    def valid_in_box(self, row_start, col_start, num):
        for r in range(row_start, row_start+3):
            for c in range(col_start, col_start+3):
                if self.board[r][c] == num:
                    return False
        return True
    # Determines if num is contained in the 3x3 box specified on the board

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num):
            if self.valid_in_col(col, num):
                if 0 <= row <= 2:
                    if 0 <= col <= 2:
                        # Check Box 1
                        if self.valid_in_box(0, 0, num):
                            return True
                    elif 3 <= col <= 5:
                        # Check Box 2
                        if self.valid_in_box(0, 3, num):
                            return True
                    elif 6 <= col <= 8:
                        # Check Box 3
                        if self.valid_in_box(0, 6, num):
                            return True
                elif 3 <= row <= 5:
                    if 0 <= col <= 2:
                        # Check Box 4
                        if self.valid_in_box(3, 0, num):
                            return True
                    elif 3 <= col <= 5:
                        # Check Box 5
                        if self.valid_in_box(3, 3, num):
                            return True
                    elif 6 <= col <= 8:
                        # Check Box 6
                        if self.valid_in_box(3, 6, num):
                            return True
                elif 6 <= row <= 8:
                    if 0 <= col <= 2:
                        # Check Box 7
                        if self.valid_in_box(6, 0, num):
                            return True
                    elif 3 <= col <= 5:
                        # Check Box 8
                        if self.valid_in_box(6, 3, num):
                            return True
                    elif 6 <= col <= 8:
                        # Check Box 9
                        if self.valid_in_box(6, 6, num):
                            return True
        return False
    # Determines if it is valid to enter num at (row, col) in the board

    def fill_box(self, row_start, col_start):
        for r in range(row_start, row_start+3):
            for c in range(col_start, col_start+3):
                while True:
                    num = randint(1, 9)
                    if self.valid_in_box(row_start, col_start, num):
                        self.board[r][c] = num
                        break
        return None
    # Fills the specified 3x3 box with values

    def fill_diagonal(self):
        self.fill_box(0,0)
        self.fill_box(3,3)
        self.fill_box(6,6)
    # Fills the three boxes along the main diagonal of the board

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
