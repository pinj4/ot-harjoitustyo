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

    def test_board_setup_is_right(self):
        correct_ans = []
        for i in range(35):
            row = []
            for j in range(15):
                row.append((255,255,255))
            correct_ans.append(row)
        self.gameloop.setup_board()
        self.assertEqual(self.gameloop.board, correct_ans)

    def test_board_setup_is_right_with_blocks(self):
        self.gameloop.blocks_on_board[(0,1)] = (0,255,0)
        self.gameloop.blocks[(0,2)] = (0,255,0)
        correct_ans = []
        for i in range(35):
            row = []
            for j in range(15):
                row.append((255,255,255))
            correct_ans.append(row)
        correct_ans[1][0] = (0,255,0)
        correct_ans[2][0] = (0,255,0)
        self.gameloop.setup_board()
        self.assertEqual(self.gameloop.board, correct_ans)


    def test_block_is_the_right_shape(self):
        block = self.gameloop.block
        if block in self.blocks.blocks:
            return True

    def test_block_is_the_right_color(self):
        block = self.gameloop.block
        if block[0]["color"] in self.blocks.blocks[0]["color"]:
            return True

    def test_block_position_is_right(self):
        block = self.gameloop.block
        self.gameloop.setup_board()
        if (block[0], block[1]) in self.gameloop.board:
            return True

    def test_is_block_at_the_tetris_board(self):
        board = [(j,i) for i in range(len(self.gameloop.board))
                for j in range(len(self.gameloop.board[i]))]
        if (self.gameloop.block[1], self.gameloop.block[2]) in board:
            return True

    def test_block_is_moving_down(self):
        block = self.gameloop.block
        self.gameloop.block_moves("down")
        self.assertEqual((block[1], block[2]), (0,1))
        self.assertEqual(self.gameloop._can_move(), True)

    def test_block_is_moving_right(self):
        block = self.gameloop.block
        self.gameloop.block_moves("right")
        self.assertEqual((block[1], block[2]), (1,0))

    def test_block_is_moving_left(self):
        block = self.gameloop.block
        self.gameloop.block_moves("left")
        self.assertEqual((block[1], block[2]), (-1,0))

    def test_block_doesnt_move_past_left_border(self):
        self.gameloop.block = [self.blocks.square, 0, 0]
        for i in range(20):
            self.gameloop.block_moves("left")
            self.gameloop._can_move()
        self.assertEqual(self.gameloop.filled_in[0][0], 0)

    def test_block_doesnt_move_past_right_border(self):
        self.gameloop.block = [self.blocks.square, 0, 0]
        for i in range(20):
            self.gameloop.block_moves("right")
            self.gameloop._can_move()
        self.assertEqual(self.gameloop.filled_in[0][0], 13)

    def test_block_doesnt_move_too_far(self):
        self.gameloop.block = [self.blocks.square, 0, 0]
        for i in range(25):
            self.gameloop.block_moves("down")
            self.gameloop._can_move()
        self.assertEqual(self.gameloop._can_move(), False)

    def test_block_doesnt_overlap_with_other_block(self):
        self.gameloop.blocks_on_board[(0, 2)] = (0,0,0)
        self.gameloop.filled_in.append((0,1))
        self.assertEqual(self.gameloop._can_move(), False)

    def test_block_stop_works(self):
        self.gameloop.blocks[(0,2)] = (0,0,0)
        self.gameloop.block_stop()
        self.assertEqual(self.gameloop.blocks_on_board[(0,2)], self.gameloop.blocks[(0,2)])

    def test_block_rotate_rotates(self):
        block = self.gameloop.block
        self.gameloop.block_rotate()
        self.assertEqual(block[0]["shape"][1], block[0]["shape"][self.gameloop.rotation])

    def test_block_rotate_work_with_multiple_rotations(self):
        self.gameloop.block = [self.blocks.stick, 0, 0]
        self.gameloop.block_rotate()
        self.gameloop.block_rotate()
        self.assertEqual(self.gameloop.rotation, 0)

    def test_clear_row_works(self):
        for i in range(len(self.gameloop.board[34])):
            self.gameloop.board[34][i] = (0, 255, 0)
        self.gameloop.clear_row()
        correct_ans = []
        for i in range(len(self.gameloop.board[34])):
            correct_ans.append((255,255,255))
        self.assertEqual(correct_ans, self.gameloop.board[0])

    def test_score_changes(self):
        for i in range(len(self.gameloop.board[34])):
            self.gameloop.board[34][i] = (0, 255, 0)
        self.gameloop.clear_row()
        self.assertEqual(10, self.gameloop.score)

    def test_changes_pieces(self):
        self.gameloop.block_stop()
        self.assertEqual(True, self.gameloop.get_new_block)

    def test_change_block_works(self):
        self.gameloop.get_new_block = True
        old_next_block = self.gameloop._next_block
        self.gameloop.change_block()
        self.assertEqual(self.gameloop.block, old_next_block)
        self.assertEqual(self.gameloop.get_new_block, False)
