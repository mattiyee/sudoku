import pygame
from constants import *


class Cell:
    # Constructor for the Cell class
    def __init__(self, value, col, row, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen

    # Function that sets the cell’s value
    def set_cell_value(self, value):
        self.value = value

    # Function that sets the cell’s sketched value
    def set_sketched_value(self, value):
        self.sketched_value = value

    # Function that draws the cell, along with the value inside it
    def draw(self):
        num_font = pygame.font.Font(None, 70)
        x_points = [114, 186, 261, 334, 411, 486, 559, 636, 711, 784]
        y_points = [104, 179, 254, 329, 404, 479, 554, 629, 704, 779]

        # Red outline

        # Left edge
        pygame.draw.line(self.screen,
                         BOX_COLOR,
                         ((x_points[self.col]) + 3, y_points[self.row]),
                         ((x_points[self.col]) + 3, (y_points[self.row+1]) - 6), 7)

        # Top edge
        pygame.draw.line(self.screen,
                         BOX_COLOR,
                         ((x_points[self.col]) + 3, (y_points[self.row]) + 1),
                         ((x_points[self.col+1]), (y_points[self.row]) + 1), 7)
        # Right edge
        pygame.draw.line(self.screen,
                         BOX_COLOR,
                         ((x_points[self.col+1] - 2), y_points[self.row]),
                         ((x_points[self.col+1] - 2), (y_points[self.row+1]) - 6), 7)

        # Bottom edge
        pygame.draw.line(self.screen,
                         BOX_COLOR,
                         ((x_points[self.col]) + 3, (y_points[self.row+1]) - 6),
                         ((x_points[self.col+1]), (y_points[self.row+1]) - 6), 7)
        '''
        pygame.draw.line(self.screen,
                         BOX_COLOR,
                         ((x_points[self.col-1]) + 3, y_points[self.row-1]),
                         ((x_points[self.col-1]) + 3, (y_points[self.row]) - 6), 7)
        pygame.draw.line(self.screen,
                         BOX_COLOR,
                         ((x_points[self.col-1]) + 3, (y_points[self.row-1]) + 1),
                         ((x_points[self.col]), (y_points[self.row-1]) + 1), 7)
        pygame.draw.line(self.screen,
                         BOX_COLOR,
                         ((x_points[self.col] - 2), y_points[self.row - 1]),
                         ((x_points[self.col] - 2), (y_points[self.row]) - 6), 7)
        pygame.draw.line(self.screen,
                         BOX_COLOR,
                         ((x_points[self.col-1]) + 3, (y_points[self.row]) - 6),
                         ((x_points[self.col]), (y_points[self.row]) - 6), 7)
        '''

        # Change the size
        if self.value != 0:
            print(self.col, self.row)
            num_surf = num_font.render(f"{self.value}", 0, FONT_COLOR)
            num_rect = num_surf.get_rect(center=(x_points[self.col - 1] + 37, y_points[self.row - 1] + 37))
            self.screen.blit(num_surf, num_rect)
            # FIXME: This should only work for inputting new values
            # FIXME: Should output different colored font to determine between sketched and actual cells
            # FIXME: Should modify list when pressing enter and remain on list after each .blit

    # If this cell has a nonzero value, that value is displayed.
    # Otherwise, no value is displayed in the cell.

    # The cell is outlined red if it is currently selected.
