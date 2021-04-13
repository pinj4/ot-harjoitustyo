import os
import pygame

dirname = os.path.dirname(__file__)

class Background(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "background.png")
            )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y