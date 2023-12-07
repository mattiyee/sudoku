import pygame, copy
from cell import Cell
from sudoku_generator import *
from constants import *


class Board:
    def __init__(self, width, height, screen, difficulty): # initializes variables
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []
        self.board = None
        self.original_board = None
        self.answer_board = None
        self.value = 0
        self.selected = None

    def initialize_board(self):
        if self.difficulty == 'Easy':
            self.board = SudokuGenerator(9, 30)
            # Change back to 30 after debugging
        elif self.difficulty == 'Medium':
            self.board = SudokuGenerator(9, 40)
        elif self.difficulty == 'Hard':
            self.board = SudokuGenerator(9, 50)
        self.board.fill_values()
        self.answer_board = self.board.get_board()
        self.board.remove_cells()
        self.original_board = copy.deepcopy(self.board.get_board())
        self.board = copy.deepcopy(self.board.get_board())
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]
        # self.board.print_board()  # debugging

    def draw(self):
        font_title = pygame.font.Font(None, 45)
        font_difficulty = pygame.font.Font(None, 30)
        num_font = pygame.font.Font(None, 70)
        x_points = [114, 186, 261, 334, 411, 486, 559, 636, 711, 784]
        y_points = [104, 179, 254, 329, 404, 479, 554, 629, 704, 779]

        surface_title = font_title.render("Sudoku", 0, LINE_COLOR)
        rectangle_title = surface_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 410))
        self.screen.blit(surface_title, rectangle_title)

        surface_difficulty = font_difficulty.render(f"Difficulty: {self.difficulty}", 0, LINE_COLOR)
        rectangle_difficulty = surface_difficulty.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 379))
        self.screen.blit(surface_difficulty, rectangle_difficulty)

        for num in range(0, 10): # for each row and column, draw a line
            if num % 3 == 0: # every third line should be bolded
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (111, self.width / 12 * num + 100),
                    (788, self.width / 12 * num + 100),
                    6
                )

                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (self.height / 12 * num + 112.5, 98),
                    (self.height / 12 * num + 112.5, 777),
                    6
                )
            else: # if row/column not divisible by 3, then it should print a normal line
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (111, self.width / 12 * num + 100),
                    (788, self.width / 12 * num + 100),
                )
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (self.height / 12 * num + 112.5, 98),
                    (self.height / 12 * num + 112.5, 777),
                )

        for r in range(9):
            for c in range(9):
                # FIXME: self.value should output an integer from the list that will print onto the board through func
                # FIXME: These functions require a condition so they cannot be changed through user input
                #   (cannot type in the box)
                if self.board[r][c] == int(0):
                    num_surf = num_font.render(" ", 0, FONT_COLOR)
                    num_rect = num_surf.get_rect(center=(x_points[c] + 37, y_points[r] + 37))
                    self.screen.blit(num_surf, num_rect)
                else:
                    num_surf = num_font.render(f"{self.board[r][c]}", 0, FONT_COLOR)
                    num_rect = num_surf.get_rect(center=(x_points[c] + 37, y_points[r] + 37))
                    self.screen.blit(num_surf, num_rect)

                # Changed self.board to list
                # self.board is a SudokuGenerator object
                    # Threw a type error whenever tried to index SudokuGenerator object
                # self.board.get_board() is a list
                # Should've used get_board() while assigning SudokuGenerator object to self.board

    def select(self, col, row, value):
        self.value = value
        self.selected = Cell(self.value, col, row, self.screen)
        self.selected.draw()

    def click(self, x, y):
        x_points = [111, 186, 261, 336, 411, 486, 561, 636, 711, 786]
        # board x is bit wider compared to cell x
        y_points = [104, 179, 254, 329, 404, 479, 554, 629, 704, 779]

        col, row = 0, 0
        if 111 <= x <= 786 and 104 <= y <= 779:
            for num in range(10):  # originally 10 instead of 1,8
                if x_points[num - 1] <= x <= x_points[num]:
                    break
                else:
                    col += 1
            for num in range(10):
                if y_points[num - 1] <= y <= y_points[num]:
                    break
                else:
                    row += 1
            return col, row
        return None

    def clear(self):
        num_font = pygame.font.Font(None, 70)
        x_points = [114, 186, 261, 334, 411, 486, 559, 636, 711, 784]
        y_points = [104, 179, 254, 329, 404, 479, 554, 629, 704, 779]
        r, c = self.selected.row, self.selected.col

        if self.board[r][c] != 0 and self.original_board[r][c] == 0:
            self.board[r][c] = int(0)
            num_surf = num_font.render("", 0, FONT_COLOR)
            num_rect = num_surf.get_rect(center=(x_points[c] + 37, y_points[r] + 37))
            self.screen.blit(num_surf, num_rect)
            pygame.display.update()

    def sketch(self, value):
        if self.selected:
            row, col = self.selected.row, self.selected.col
            # self.selected

    # Update self.board 2D list with integers
    def place_number(self, value):
        num_font = pygame.font.Font(None, 70)
        x_points = [114, 186, 261, 334, 411, 486, 559, 636, 711, 784]
        y_points = [104, 179, 254, 329, 404, 479, 554, 629, 704, 779]
        r, c = self.selected.row, self.selected.col

        if self.board[r][c] == 0:
            self.board[r][c] = value
        num_surf = num_font.render(f"{self.board[r][c]}", 0, FONT_COLOR)
        num_rect = num_surf.get_rect(center=(x_points[c] + 37, y_points[r] + 37))
        self.screen.blit(num_surf, num_rect)

    # Resets the board
    def reset_to_original(self):
        self.board = self.original_board

    def is_full(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    # Update self.cells 2D list with Cell objects
    def update_board(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]

    def find_empty(self):
        for row in self.board:
            if 0 in row:
                return row.index(0), self.board.index(row)

    def check_board(self):
        if self.board == self.answer_board:
            return True
        return False
