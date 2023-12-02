import pygame, sys, board
from sudoku_generator import SudokuGenerator
from constants import *


def draw_game_start(screen):
    font_start = pygame.font.Font(None, 100)
    font_authors = pygame.font.Font(None, 30)
    font_gamemode = pygame.font.Font(None, 80)
    font_button = pygame.font.Font(None, 60)
    # Initializing fonts

    screen.fill(BG_COLOR)
    background = pygame.image.load("sudoku.png")
    screen.blit(background, (0, 0))

    surface_title = font_start.render("Welcome to Sudoku", 0, LINE_COLOR)
    rectangle_title = surface_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(surface_title, rectangle_title)

    surface_authors = font_authors.render(
        "Created by Preston Hemmy, Thurstan Ngo, Ephraim Nicolas, and Matthew Yee", 0, LINE_COLOR)
    rectangle_authors = surface_authors.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 135))
    screen.blit(surface_authors, rectangle_authors)

    surface_gamemode = font_gamemode.render("Select a game mode:", 0, LINE_COLOR)
    rectangle_gamemode = surface_gamemode.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 5))
    screen.blit(surface_gamemode, rectangle_gamemode)
    # Initializing non-button text

    easy_text = font_button.render("Easy", 0, LINE_COLOR)
    medium_text = font_button.render("Medium", 0, LINE_COLOR)
    hard_text = font_button.render("Hard", 0, LINE_COLOR)

    surface_easy = pygame.Surface((easy_text.get_size()[0] + 80, easy_text.get_size()[1] + 40))
    surface_easy.fill(BUTTON_COLOR)
    surface_easy.blit(surface_easy, (10, 10))
    rectangle_easy = surface_easy.get_rect(center=(WIDTH // 2 - 275, HEIGHT // 2 + 124))
    screen.blit(surface_easy, rectangle_easy)
    screen.blit(easy_text, (125, 555))

    surface_medium = pygame.Surface((medium_text.get_size()[0] + 80, medium_text.get_size()[1] + 40))
    surface_medium.fill(BUTTON_COLOR)
    surface_medium.blit(surface_medium, (10, 10))
    rectangle_medium = surface_medium.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 124))
    screen.blit(surface_medium, rectangle_medium)
    screen.blit(medium_text, (373, 555))

    surface_hard = pygame.Surface((hard_text.get_size()[0] + 80, hard_text.get_size()[1] + 40))
    surface_hard.fill(BUTTON_COLOR)
    surface_hard.blit(surface_hard, (10, 10))
    rectangle_hard = surface_hard.get_rect(center=(WIDTH // 2 + 275, HEIGHT // 2 + 124))
    screen.blit(surface_hard, rectangle_hard)
    screen.blit(hard_text, (677, 555))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rectangle_easy.collidepoint(event.pos):
                    return "easy"
                elif rectangle_medium.collidepoint(event.pos):
                    return "medium"
                elif rectangle_hard.collidepoint(event.pos):
                    return "hard"
        pygame.display.update()
# Function that draws the game start screen


def draw_game_over(screen):
    pass
# Function that draws the game over screen


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Sudoku")

    gamemode = draw_game_start(screen)

    # board123 = board.Board(700, 700, screen, 1)
    # board123.draw()

    screen.fill(BG_COLOR)

    # Call draw_game_start()
    # draw_game_start(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #  if event.type == pygame.display.set_mode(900, 900)
            if gamemode == "easy":
                my_sudoku = SudokuGenerator(9, 30)
                my_sudoku.print_board()
                # FIXME: Infinite loop, code for proper gamemode
            if gamemode == "medium":
                my_sudoku = SudokuGenerator(9, 40)
                my_sudoku.print_board()
                # FIXME: Infinite loop, code for proper gamemode
            if gamemode == "hard":
                my_sudoku = SudokuGenerator(9, 50)
                my_sudoku.print_board()
                # FIXME: Infinite loop, code for proper gamemode
        pygame.display.update()
