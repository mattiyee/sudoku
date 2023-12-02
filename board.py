import pygame
class Board:
    def __init__(self, width, height, screen, difficulty): # initializes variables
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        for num in range(0, 10): # for each row and column, draw a line
            if num % 3 == 0: # every third line should be bolded
                pygame.draw.line(
                    self.screen,
                    (255, 255, 255),
                    (0, self.width / 9 * num),
                    (self.width, self.width / 9 * num),
                    6
                )
                pygame.draw.line(
                    self.screen,
                    (255, 255, 255),
                    (self.height / 9 * num, 0),
                    (self.height / 9 * num, self.height),
                    6
                )
            else: # if row/column not divisible by 3, then it should print a normal line
                pygame.draw.line(
                    self.screen,
                    (255, 255, 255),
                    (0, self.width / 9 * num),
                    (self.width, self.width / 9 * num),
                )
                pygame.draw.line(
                    self.screen,
                    (255, 255, 255),
                    (self.height / 9 * num, 0),
                    (self.height / 9 * num, self.height),
                )

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass