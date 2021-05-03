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
    
    def test_block_is_moving_down(self):
        block = self.gameloop.block
        self.gameloop.block_moves("down")
        self.assertEqual((block[1], block[2]), (0,1))
    
    def test_block_is_moving_right(self):
        block = self.gameloop.block
        self.gameloop.block_moves("right")
        self.assertEqual((block[1], block[2]), (1,0))
    
    def test_block_is_moving_left(self):
        block = self.gameloop.block
        self.gameloop.block_moves("left")
        self.assertEqual((block[1], block[2]), (-1,0))

    def test_block_rotate_rotates(self):
        block = self.gameloop.block
        self.gameloop.block_rotate()
        self.assertEqual(block[0]["shape"][1], block[0]["shape"][self.gameloop.rotation])
    
    def test_clear_row_works(self):
        for i in range(len(self.gameloop.board[39])):
            self.gameloop.board[39][i] = (0, 255, 0)
        self.gameloop.clear_row()
        correct_ans = []
        for i in range(len(self.gameloop.board[39])):
            correct_ans.append((255,255,255))
        self.assertEqual(correct_ans, self.gameloop.board[0])
    
    def test_score_changes(self):
        for i in range(len(self.gameloop.board[39])):
            self.gameloop.board[39][i] = (0, 255, 0)
        self.gameloop.clear_row()
        self.assertEqual(10, self.gameloop.score)
    
    def test_changes_pieces(self):
        self.gameloop._block_stop()
        self.assertEqual(True, self.gameloop.get_new_block)



    
