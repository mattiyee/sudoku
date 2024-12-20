import pygame, sys
from pygame.locals import *
from board import Board
from sudoku_generator import *
from constants import *
from cell import Cell


# Creates and displays the game start screen
def draw_game_start(screen):
    # Initializing fonts
    font_start = pygame.font.Font(None, 100)
    font_authors = pygame.font.Font(None, 30)
    font_gamemode = pygame.font.Font(None, 80)
    font_button = pygame.font.Font(None, 60)
    font_quit_button = pygame.font.Font(None, 40)

    screen.fill(BG_COLOR)
    background = pygame.image.load("sudoku.png")
    screen.blit(background, (0, 0))

    # Initializing non-button text
    surface_title = font_start.render("Welcome to Sudoku", 0, LINE_COLOR)
    rectangle_title = surface_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(surface_title, rectangle_title)

    surface_authors = font_authors.render(
        "Created by Matthew Yee, Thurstan Ngo, Ephraim Nicolas, and Preston Hemmy", 0, LINE_COLOR)
    rectangle_authors = surface_authors.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 135))
    screen.blit(surface_authors, rectangle_authors)

    surface_gamemode = font_gamemode.render("Select a game mode:", 0, LINE_COLOR)
    rectangle_gamemode = surface_gamemode.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 5))
    screen.blit(surface_gamemode, rectangle_gamemode)


    # Initalizing button text
    easy_text = font_button.render("Easy", 0, LINE_COLOR)
    medium_text = font_button.render("Medium", 0, LINE_COLOR)
    hard_text = font_button.render("Hard", 0, LINE_COLOR)
    quit_text = font_quit_button.render("Quit", 0, LINE_COLOR)

    # Easy button
    surface_easy = pygame.Surface((easy_text.get_size()[0] + 80, easy_text.get_size()[1] + 40))
    surface_easy.fill(BUTTON_COLOR)
    surface_easy.blit(surface_easy, (10, 10))
    rectangle_easy = surface_easy.get_rect(center=(WIDTH // 2 - 275, HEIGHT // 2 + 124))
    screen.blit(surface_easy, rectangle_easy)
    screen.blit(easy_text, (125, 556))

    # Medium button
    surface_medium = pygame.Surface((medium_text.get_size()[0] + 80, medium_text.get_size()[1] + 40))
    surface_medium.fill(BUTTON_COLOR)
    surface_medium.blit(surface_medium, (10, 10))
    rectangle_medium = surface_medium.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 124))
    screen.blit(surface_medium, rectangle_medium)
    screen.blit(medium_text, (373, 556))

    # Hard button
    surface_hard = pygame.Surface((hard_text.get_size()[0] + 80, hard_text.get_size()[1] + 40))
    surface_hard.fill(BUTTON_COLOR)
    surface_hard.blit(surface_hard, (10, 10))
    rectangle_hard = surface_hard.get_rect(center=(WIDTH // 2 + 275, HEIGHT // 2 + 124))
    screen.blit(surface_hard, rectangle_hard)
    screen.blit(hard_text, (677, 556))

    # Quit button
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

# Creates and displays the game over screen
def draw_game_over(screen, status):
    # Initializing fonts
    font_game = pygame.font.Font(None, 100)
    font_subtext = pygame.font.Font(None, 45)
    font_button = pygame.font.Font(None, 60)
    text = ""
    subtext = ""

    screen.fill(BG_COLOR)
    background = pygame.image.load("sudoku.png")
    screen.blit(background, (0, 0))

    if status == 1:
        text = "Game Won!"
        subtext = "You completed the board successfully!"
    elif status == 2:
        text = "Game Over! :("
        subtext = "Better luck next time!"

    surface_game = font_game.render(text, 0, LINE_COLOR)
    rectangle_game = surface_game.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(surface_game, rectangle_game)

    surface_subtext = font_subtext.render(subtext, 0, LINE_COLOR)
    rectangle_subtext = surface_subtext.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 135))
    screen.blit(surface_subtext, rectangle_subtext)

    reset_text = font_button.render("Reset", 0, LINE_COLOR)
    quit_text = font_button.render("Quit", 0, LINE_COLOR)

    # Reset button
    surface_reset = pygame.Surface((reset_text.get_size()[0] + 80, reset_text.get_size()[1] + 40))
    surface_reset.fill(BUTTON_COLOR)
    surface_reset.blit(surface_reset, (10, 10))
    rectangle_reset = surface_reset.get_rect(center=(WIDTH // 2 - 200, HEIGHT // 2 + 124))
    screen.blit(surface_reset, rectangle_reset)
    screen.blit(reset_text, (192, 556))

    # Quit button
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

# Buttons on the in progress screen
def board_buttons(screen):
    surface_reset.fill(BUTTON_COLOR)
    surface_reset.blit(surface_reset, (10, 10))
    screen.blit(surface_reset, rectangle_reset)
    screen.blit(reset_text, (283, 822))

    surface_quit.fill(BUTTON_COLOR)
    surface_quit.blit(surface_quit, (10, 10))
    screen.blit(surface_quit, rectangle_quit)
    screen.blit(quit_text, (544, 822))

# Displays the buttons on the in progress screen
def menu(screen):
    screen.fill(SUDOKU_BG_COLOR)
    board_buttons(screen)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Sudoku")

    font_button = pygame.font.Font(None, 45)
    reset_text = font_button.render("Reset", 0, LINE_COLOR)
    quit_text = font_button.render("Quit", 0, LINE_COLOR)
    surface_reset = pygame.Surface((reset_text.get_size()[0] + 45, reset_text.get_size()[1] + 35))
    surface_quit = pygame.Surface((quit_text.get_size()[0] + 65, quit_text.get_size()[1] + 35))
    rectangle_reset = surface_reset.get_rect(center=(WIDTH // 2 - 125, HEIGHT // 2 + 385))
    rectangle_quit = surface_quit.get_rect(center=(WIDTH // 2 + 125, HEIGHT // 2 + 385))

    sudoku_board = Board(900, 900, screen, draw_game_start(screen))
    sudoku_board.initialize_board()
    sudoku_board.draw()
    pygame.display.update()
    menu(screen)
    square_size = 700
    game_over = False
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # User clicks on cell
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if rectangle_reset.collidepoint(event.pos):

                    sudoku_board = Board(900, 900, screen, draw_game_start(screen))
                    sudoku_board.initialize_board()
                    sudoku_board.draw()
                    pygame.display.update()
                    menu(screen)
                    square_size = 700
                    game_over = False
                if rectangle_quit.collidepoint(event.pos):
                    sys.exit()

                square_num = 0
                x, y = pygame.mouse.get_pos()  # x = col, y = row
                x, y = sudoku_board.click(x, y)
                screen.fill(SUDOKU_BG_COLOR)
                sudoku_board.draw()
                board_buttons(screen)
                sudoku_board.select(x-1, y-1, square_num)

            # User deletes number in cell
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                sudoku_board.clear()
                sudoku_board.update_board()
                menu(screen)
                sudoku_board.draw()
                game_over = False

            # User types a sketched number on keyboard
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    sudoku_board.sketch(1)
                elif event.key == pygame.K_2:
                    sudoku_board.sketch(2)
                elif event.key == pygame.K_3:
                    sudoku_board.sketch(3)
                elif event.key == pygame.K_4:
                    sudoku_board.sketch(4)
                elif event.key == pygame.K_5:
                    sudoku_board.sketch(5)
                elif event.key == pygame.K_6:
                    sudoku_board.sketch(6)
                elif event.key == pygame.K_7:
                    sudoku_board.sketch(7)
                elif event.key == pygame.K_8:
                    sudoku_board.sketch(8)
                elif event.key == pygame.K_9:
                    sudoku_board.sketch(9)
                sudoku_board.update_board()

            # User confirms the value in a cell
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                sudoku_board.place_number()
                sudoku_board.update_board()

            # Checks if the board is filled in correctly
            if sudoku_board.is_full():
                if sudoku_board.check_board():
                    game_over = True
                    win = True
                    break
                else:
                    game_over = True
                    win = False
                    break

        if game_over:
            pygame.display.update()
            if win:
                draw_game_over(screen, 1)
            else:
                draw_game_over(screen, 2)
            game_over = False

        pygame.display.update()
        game_over = False
