import unittest
import pygame
from blocks import Blocks
from gameloop import GameLoop
from main import Tetris

class TestTetris(unittest.TestCase):

    def setUp(self):
        self.tetris = Tetris()
        self.display = pygame.display.set_mode((800,700))
        self.gameloop = GameLoop(self.display)
        self.blocks = Blocks()

    def test_block_is_the_right_shape(self):
        block = self.gameloop.block
        if block in self.blocks.blocks:
            return True
    
    def test_block_is_the_right_color(self):
        block = self.gameloop.block
        if block[0]["color"] in self.blocks.blocks[0]["color"]:
            return True
    
    def test_is_block_at_the_tetris_board(self):
        board = [(j,i) for i in range(len(self.gameloop.board)) for j in range(len(self.gameloop.board[i]))]
        if (self.gameloop.block[1], self.gameloop.block[2]) in board:
            return True
    
    def test_block_is_moving(self):
        block = self.gameloop.block
        self.gameloop.block_moves(block, "down")
        self.assertEqual((block[1], block[2]), (0,1))

    
