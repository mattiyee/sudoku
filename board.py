import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator
from constants import *


class Board:
    def __init__(self, width, height, screen, difficulty): # initializes variables
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        # self.updated_board = self.board
        self.cells = None
        self.board = None
        self.answer_board = None
        self.selected = None

    def initialize_board(self):
        if self.difficulty == 'Easy':
            self.board = SudokuGenerator(9, 30)
        elif self.difficulty == 'Medium':
            self.board = SudokuGenerator(9, 40)
        elif self.difficulty == 'Hard':
            self.board = SudokuGenerator(9, 50)
        self.board.fill_values()
        self.answer_board = self.board.get_board()
        self.board.remove_cells()
        self.cells = [[Cell(self.board, i, j, self.screen) for j in range(9)] for i in range(9)]

    def draw(self):
        font_title = pygame.font.Font(None, 45)
        font_difficulty = pygame.font.Font(None, 30)

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

    def select(self, row, col):
        self.selected = Cell(self.board[row][col], row, col, self.screen)
        self.selected.draw()

    def click(self, x, y):
        x_points = [111, 186, 261, 336, 411, 486, 561, 636, 711, 786]
        y_points = [104, 179, 254, 329, 404, 479, 554, 629, 704, 779]

        col, row = 0, 0
        if 111 <= x <= 786 and 104 <= y <= 779:
            for num in range(10):
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

        # if 115 <= x <= 787:
            # if 104 <= y <= 775:
                # return int(y // (self.width / 12)), int(x // (self.height / 12))
        # return None

    def clear(self):
        if self.selected:
            row, col = self.selected.row, self.selected.col
            self.board[row][col] = 0

    def sketch(self, value):
        if self.selected:
            row, col = self.selected.row, self.selected.col
            self.board[row][col] = value

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def update_board(self):
        pass

    def find_empty(self):
        for row in self.board:
            if 0 in row:
                return row.index(0), self.board.index(row)

    def check_board(self):
        if self.board == self.answer_board:
            return True
        return False