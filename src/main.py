import pygame
from level import Level
from gameloop import GameLoop



def main():
    display_width= 370
    display_height = 420
    
    white = 0xFFFFFF
    display = pygame.display.set_mode((display_width, display_height))
    display.fill(white)
    pygame.display.set_caption("TETRIS")

    pygame.init()

    level = Level()
    gameloop = GameLoop(level, display)
    gameloop.start()


main()

