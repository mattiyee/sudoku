import pygame, sys, board
from sudoku_generator import SudokuGenerator
from constants import *


def draw_game_start(screen):
    font_start = pygame.font.Font(None, 100)
    font_authors = pygame.font.Font(None, 30)
    font_gamemode = pygame.font.Font(None, 80)
    font_button = pygame.font.Font(None, 60)
    font_quit_button = pygame.font.Font(None, 40)
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
    quit_text = font_quit_button.render("Quit", 0, LINE_COLOR)

    surface_easy = pygame.Surface((easy_text.get_size()[0] + 80, easy_text.get_size()[1] + 40))
    surface_easy.fill(BUTTON_COLOR)
    surface_easy.blit(surface_easy, (10, 10))
    rectangle_easy = surface_easy.get_rect(center=(WIDTH // 2 - 275, HEIGHT // 2 + 124))
    screen.blit(surface_easy, rectangle_easy)
    screen.blit(easy_text, (125, 556))

    surface_medium = pygame.Surface((medium_text.get_size()[0] + 80, medium_text.get_size()[1] + 40))
    surface_medium.fill(BUTTON_COLOR)
    surface_medium.blit(surface_medium, (10, 10))
    rectangle_medium = surface_medium.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 124))
    screen.blit(surface_medium, rectangle_medium)
    screen.blit(medium_text, (373, 556))

    surface_hard = pygame.Surface((hard_text.get_size()[0] + 80, hard_text.get_size()[1] + 40))
    surface_hard.fill(BUTTON_COLOR)
    surface_hard.blit(surface_hard, (10, 10))
    rectangle_hard = surface_hard.get_rect(center=(WIDTH // 2 + 275, HEIGHT // 2 + 124))
    screen.blit(surface_hard, rectangle_hard)
    screen.blit(hard_text, (677, 556))

    surface_quit = pygame.Surface((quit_text.get_size()[0] + 70, quit_text.get_size()[1] + 30))
    surface_quit.fill(BUTTON_COLOR)
    surface_quit.blit(surface_quit, (10, 10))
    rectangle_quit = surface_quit.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 275))
    screen.blit(surface_quit, rectangle_quit)
    screen.blit(quit_text, (420, 713))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rectangle_quit.collidepoint(event.pos):
                    sys.exit()
                elif rectangle_easy.collidepoint(event.pos):
                    return "Easy"
                elif rectangle_medium.collidepoint(event.pos):
                    return "Medium"
                elif rectangle_hard.collidepoint(event.pos):
                    return "Hard"
        pygame.display.update()
# Function that draws the game start screen


def draw_game_over(screen, status):
    font_game = pygame.font.Font(None, 100)
    font_subtext = pygame.font.Font(None, 45)
    font_button = pygame.font.Font(None, 60)
    text = ""
    subtext = ""
    # Initializing fonts

    screen.fill(BG_COLOR)
    background = pygame.image.load("sudoku.png")
    screen.blit(background, (0, 0))

    if status == 1:
        text = "Game Over! :("
        subtext = "Better luck next time!"
    elif status == 2:
        text = "Game Won!"
        subtext = "You completed the board successfully!"

    surface_game = font_game.render(text, 0, LINE_COLOR)
    rectangle_game = surface_game.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(surface_game, rectangle_game)

    surface_subtext = font_subtext.render(subtext, 0, LINE_COLOR)
    rectangle_subtext = surface_subtext.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 135))
    screen.blit(surface_subtext, rectangle_subtext)

    reset_text = font_button.render("Reset", 0, LINE_COLOR)
    quit_text = font_button.render("Quit", 0, LINE_COLOR)

    surface_reset = pygame.Surface((reset_text.get_size()[0] + 80, reset_text.get_size()[1] + 40))
    surface_reset.fill(BUTTON_COLOR)
    surface_reset.blit(surface_reset, (10, 10))
    rectangle_reset = surface_reset.get_rect(center=(WIDTH // 2 - 200, HEIGHT // 2 + 124))
    screen.blit(surface_reset, rectangle_reset)
    screen.blit(reset_text, (192, 556))

    surface_quit = pygame.Surface((quit_text.get_size()[0] + 80, quit_text.get_size()[1] + 40))
    surface_quit.fill(BUTTON_COLOR)
    surface_quit.blit(surface_quit, (10, 10))
    rectangle_quit = surface_quit.get_rect(center=(WIDTH // 2 + 200, HEIGHT // 2 + 124))
    screen.blit(surface_quit, rectangle_quit)
    screen.blit(quit_text, (606, 556))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rectangle_quit.collidepoint(event.pos):
                    sys.exit()
                elif rectangle_reset.collidepoint(event.pos):
                    return draw_game_start(screen)
        pygame.display.update()

# Function that draws the game over screen


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Sudoku")

    gamemode = draw_game_start(screen)
    screen.fill(BG_COLOR)

    board123 = board.Board(700, 700, screen, 1)
    board123.draw()

    square_size = 700
    # Call draw_game_start()
    # draw_game_start(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
            #  if event.type == pygame.display.set_mode(900, 900)

            # sudoku_board = board.Board(700, 700, screen, gamemode)
            # sudoku_board.initialize_board()
            # sudoku_board.draw()
            # FIXME: Produces TypeError

            '''
            if sudoku_board.check_board() == True:
                draw_game_over(screen, 1)
            if sudoku_board.check_board == False:
                draw_game_over(screen, 2)
            # FIXME: This should only be run once the entire board is complete.

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     x, y = event.pos
            #     row = y // (square_size / 9)
            #     col = x // (square_size / 9)
            '''
