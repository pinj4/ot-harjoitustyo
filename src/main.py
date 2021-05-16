import pygame
from gameloop import GameLoop


class Tetris:
    def __init__(self):
        pass

    def play(self):

        pygame.init()

        display = pygame.display.set_mode((800,700))
        display.fill((230,210,170))
        pygame.display.set_caption("TETRIS")

        gameloop = GameLoop(display)

        font = pygame.font.SysFont("comicsans",60, bold = True)
        title = font.render("TETRIS", 1, (210, 150, 75))
        font = pygame.font.SysFont("comicsans",30)
        next_piece = font.render("NEXT PIECE:", 1, (210, 150, 75))
        high_score = font.render("HIGH SCORE:", 1, (210, 150, 75))
        font = pygame.font.SysFont("comicsans",40)
        score = font.render(gameloop.hscore, 1, (210, 150, 75))

        display.blit(title, (250, 50))
        display.blit(next_piece, (600, 100))
        display.blit(high_score, (10, 100))
        display.blit(score, (10,150))

        gameloop.handle_events()

if __name__ == "__main__":
    tetris = Tetris()
    tetris.play()
    