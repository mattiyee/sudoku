import pygame
from constants import *


class Cell:
    # Constructor for the Cell class
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = None
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
        num_font = pygame.font.Font(None, 70)  # Change the size
        if self.value != 0:
            num_surf = num_font.render(str(self.value), 0, FONT_COLOR)
            num_rect = num_surf.get_rect(
                center=(WIDTH * self.col + WIDTH // 2, HEIGHT * self.row + HEIGHT // 2))
            self.screen.blit(num_surf, num_rect)


    # If this cell has a nonzero value, that value is displayed.
    # Otherwise, no value is displayed in the cell.


    # The cell is outlined red if it is currently selected.
