import pygame, sys

# Function that draws the game start screen
def draw_game_start(screen):
    pass

# Function that draws the game over screen
def draw_game_over(screen):
    pass


if __name__ == "__main__":

    pygame.init()
    screen = pygame.dispaly.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    # Call draw_game_start()
    # draw_game_start(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.