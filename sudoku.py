import pygame, sys, board
from sudoku_generator import SudokuGenerator

# Function that draws the game start screen
def draw_game_start(screen):
    pass

# Function that draws the game over screen
def draw_game_over(screen):
    pass


if __name__ == "__main__":

    '''
    my_sudoku = SudokuGenerator(0)
    my_sudoku.print_board()
    '''


    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Sudoku")
    square_size = 700
    # Call draw_game_start()
    # draw_game_start(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     x, y = event.pos
            #     row = y // (square_size / 9)
            #     col = x // (square_size / 9)

        pygame.display.update()
          #  if event.type == pygame.display.set_mode(900, 900)
