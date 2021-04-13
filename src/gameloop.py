import pygame
from level import Level

class GameLoop:
    def __init__(self, level, display):
        self._level = level
        self._clock = pygame.time.Clock()
        self._display = display

        self._level = Level()

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            self._render()
            self._level.block_falls()
            self._level.initialize_sprites()

            pygame.display.update()
            pygame.display.flip()

            self._clock.tick(20)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.move_block(dx=-20)
                if event.key == pygame.K_RIGHT:
                    self._level.move_block(dx=20)
                if event.key == pygame.K_DOWN:
                    self._level.move_block(dy=20)

            elif event.type == pygame.QUIT:
                return False



    def _render(self):
        all_sprites = self._level.add_sprites()
        all_sprites.draw(self._display)

        pygame.display.update()

