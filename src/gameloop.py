import pygame
from board import Board
from blocks import Blocks

class GameLoop:
    def __init__(self, display):
        self._clock = pygame.time.Clock()
        self.display = display

        self.board = Board(self.display)
            
        self.board = self.board.tetris_board()   

      
        self.width = 600
        self.height = 700
        self._cell_size = 20
        self._tetris_width = self._cell_size * 15 
        self._tetris_height = self._cell_size * 30
        self._left_x = (self.width - self._tetris_width) // 2
        self._right_x = self._left_x + self.width
        self._top_y = self.height - self._tetris_height
        self._bottom_y = self._top_y + self.height

        self.blocks = {}
        self.filled_in = []
        self.blocks_on_board = {}

        self.block = Blocks()
        self._next_block = Blocks()
        self.block = self.block.new_block()
        self._next_block = self._next_block.new_block()
        self.get_new_block = False
        

        #self.fall_time = 0
    
    def setup_board(self, blocks):
        blocks = self.blocks
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (j,i) in self.blocks_on_board:
                    self.board[i][j] = self.blocks_on_board[(j,i)]
                elif (j,i) in blocks:
                    self.board[i][j] = blocks[(j,i)]
        
    
    def draw_board(self):
        self.setup_board(self.blocks)

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                rect = (self._left_x + j * self._cell_size, self._top_y + i * self._cell_size, self._cell_size, self._cell_size)
                pygame.draw.rect(self.display, self.board[i][j], rect ,0)

    
    def _can_move(self):

        for pos in self.filled_in:
            if pos[0] > 20 or pos[0] < 0:
                return False
            if pos[1] > 28 or pos[1] < 0:
                return False
            
            if (pos[0], pos[1] + 1) in self.blocks_on_board:
                return False
            
        return True
    
    
    def _block_stop(self):

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (j,i) in self.blocks and self.blocks[(j,i)] != (255,255,255):
                    self.blocks_on_board[(j,i)] = self.blocks[(j,i)]

        self.get_new_block = True
    
    def change_block(self):
        self.block = self._next_block
        self._next_block = Blocks()
        self._next_block = self._next_block.new_block()
        self.get_new_block = False
    
    def show_next_block(self):


        rect = (600, 150, self._cell_size * 20, self._cell_size*20)
        pygame.draw.rect(self.display,(230,210,170), rect ,0)

        next_block = []
        block = self._next_block
        for i in range(len(block[0]["shape"])):
            for j in range(len(block[0]["shape"][i])):
                if block[0]["shape"][i][j] == 1:
                    next_block.append((j,i)) 

        for box in next_block:
                rect = (600 + box[0] * self._cell_size,  150 + box[1] * self._cell_size, self._cell_size, self._cell_size)
                pygame.draw.rect(self.display, block[0]["color"], rect ,0)
    




    
    def block_moves(self, block, direction):
        block = self.block
        self.filled_in.clear()
    

        for i in self.blocks:
            self.blocks[i] = (255, 255, 255)


        if direction == "down":
            self.block[2] += 1

            for i in range(len(block[0]["shape"])):
                for j in range(len(block[0]["shape"][i])):
                    if block[0]["shape"][i][j] == 1:
                        self.filled_in.append((j + self.block[1], i + self.block[2]))
            
                
            for i in range(self.block[2],len(self.board)):
                for j in range(len(self.board[i])):
                    if (j,i) in self.filled_in:
                        self.blocks[(j,i)] = block[0]["color"]
    
        if direction == "up":
            self.block[2] -= 1

            for i in range(len(block[0]["shape"])):
                for j in range(len(block[0]["shape"][i])):
                    if block[0]["shape"][i][j] == 1:
                        self.filled_in.append((j + self.block[1], i + self.block[2]))
                
            for i in range(self.block[2],len(self.board)):
                for j in range(len(self.board[i])):
                    if (j,i) in self.filled_in:
                        self.blocks[(j,i)] = block[0]["color"]
        
        if direction == "right":
            self.block[1] += 1

            for i in range(len(block[0]["shape"])):
                for j in range(len(block[0]["shape"][i])):
                    if block[0]["shape"][i][j] == 1:
                        self.filled_in.append((j + self.block[1],i + self.block[2]))
        
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if (j,i) in self.filled_in:
                        self.blocks[(j,i)] = block[0]["color"]
    
            
        if direction == "left":
            self.block[1] -= 1

            for i in range(len(block[0]["shape"])):
                for j in range(len(block[0]["shape"][i])):
                    if block[0]["shape"][i][j] == 1:
                        self.filled_in.append((j + self.block[1],i + self.block[2]))
        
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if (j,i) in self.filled_in:
                        self.blocks[(j,i)] = block[0]["color"]
        
    
    def handle_events(self):
        while True:

            self.draw_board()
            pygame.display.flip()

            self.block_moves(self.block, "down")
            if self._can_move() == False:
                self._block_stop()
                self.change_block()
            self.draw_board()
            self.show_next_block()
            self._clock.tick(5)



            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.block_moves(self.block, "down")
                    if event.key == pygame.K_RIGHT:
                        self.block_moves(self.block, "right")
                    if event.key == pygame.K_LEFT:
                        self.block_moves(self.block, "left")

                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    quit()
            



#display1 = pygame.display.set_mode((600,700))
#testi = GameLoop(display1)
#block1 = Blocks()
#test_block = block1.new_block
#print(testi.block_moves(test_block))
#boardh = testi.draw_board()

#for i in range(len(boardh)):
    #print(f"i: {i}")
    #for j in range(len(boardh[i])):
        #print("j:",j)
        

 
