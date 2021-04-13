import os
import pygame

dirname = os.path.dirname(__file__)

class Blocks(pygame.sprite.Sprite):
    def __init__(self, block, x, y):
        super().__init__()
        self.block = block

        self.image = pygame.image.load(
            os.path.join(dirname, "assets", self.block)
            )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    

