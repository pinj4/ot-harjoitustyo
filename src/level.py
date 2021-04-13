
from random import randint
import pygame
from blocks import Blocks
from wall import Wall



class Level:
    def __init__(self):
        self.map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]]
        self.cell_size = 20
        self.height = len(self.map)
        self.width = len(self.map[0])


        self.blocks = pygame.sprite.Group()
        self.wall = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.initialize_sprites()
        self.add_sprites()

    def initialize_sprites(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.map[y][x]
                normalized_y = y * self.cell_size
                normalized_x = x * self.cell_size

                if cell == 1:
                    self.wall.add(Wall(normalized_x, normalized_y))
                elif cell == 2:
                    self.blocks.add(Blocks("stick.png", normalized_x, normalized_y))
                elif cell == 3:
                    self.blocks.add(Blocks("square.png", normalized_x, normalized_y))
                elif cell == 4:
                    self.blocks.add(Blocks("j_block.png", normalized_x, normalized_y))
                elif cell == 5:
                    self.blocks.add(Blocks("l_block.png", normalized_x, normalized_y))
                elif cell == 6:
                    self.blocks.add(Blocks("s_block.png", normalized_x, normalized_y))
                elif cell == 7:
                    self.blocks.add(Blocks("t_block.png", normalized_x, normalized_y))
                elif cell == 8:
                    self.blocks.add(Blocks("z_block.png", normalized_x, normalized_y))
                    
    def add_sprites(self):
        self.all_sprites.add(self.wall, self.blocks)
        return self.all_sprites
        
    def move_block(self, dx = 0, dy = 0):
        if not self._block_can_move(dx, dy):
            return False

        self.blocks.rect.move_ip(dx, dy)
    
    def _block_can_move(self, dx = 0, dy = 0):
        self.blocks.rect.move_ip(dx, dy)
        colliding_walls = pygame.sprite.spritecollide(self.blocks, self.wall, False)
        can_move = not colliding_walls
        
        self.blocks.rect.move_ip(-dx, -dy)
        return can_move
    
    def block_falls(self):
        value = randint(2,8)
        y = 0
        x = 9
        self.map[y][x] = value

        while True:
            y += 1
            if y > 19:
                break

            self.map[y][x] = value
            self.initialize_sprites()
            self.add_sprites()


    
    











