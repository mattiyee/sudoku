import pygame
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        for num in range(0, 10):
            if num % 3 == 0:
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
            else:
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