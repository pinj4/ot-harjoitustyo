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
        self.score = 0

        self.blocks = {}
        self.filled_in = []
        self.blocks_on_board = {}

        self.block = Blocks()
        self._next_block = Blocks()
        self.block = self.block.new_block()
        self._next_block = self._next_block.new_block()
        self.get_new_block = False
        self.rotation = 0
        
    
    def setup_board(self):
        blocks = self.blocks
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (j,i) in self.blocks_on_board:
                    self.board[i][j] = self.blocks_on_board[(j,i)]
                elif (j,i) in blocks:
                    self.board[i][j] = blocks[(j,i)]
        
    
    def draw_board(self):
        self.setup_board()

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                rect = (self._left_x + j * self._cell_size, self._top_y + i * self._cell_size, self._cell_size, self._cell_size)
                pygame.draw.rect(self.display, self.board[i][j], rect ,0)
        
        rect = (600, 600, self._cell_size * 20, self._cell_size*20)
        pygame.draw.rect(self.display,(230,210,170), rect ,0)
        font = pygame.font.SysFont("comicsans", 40)
        score = font.render(f"SCORE: {self.score}", 1, (210, 150, 75))
        self.display.blit(score, (600, 600))
        pygame.display.flip()

    
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
        self.rotation = 0
    
    def show_next_block(self):
        rect = (600, 150, self._cell_size * 20, self._cell_size*20)
        pygame.draw.rect(self.display,(230,210,170), rect ,0)
        
        block = self._next_block
        next_block = []
        for i in range(len(block[0]["shape"][0])):
            for j in range(len(block[0]["shape"][0][i])):
                if block[0]["shape"][0][i][j] == "1":
                    next_block.append((j,i)) 

        for box in next_block:
                rect = (600 + box[0] * self._cell_size,  150 + box[1] * self._cell_size, self._cell_size, self._cell_size)
                pygame.draw.rect(self.display, block[0]["color"], rect ,0)
    


    def block_rotate(self):
        self.rotation += 1
        if self.rotation >= len(self.block[0]["shape"]):
            self.rotation = 0


    def block_moves(self, direction):
        self.filled_in.clear()
    

        for i in self.blocks:
            self.blocks[i] = (255, 255, 255)

        block = self.block[0]["shape"][self.rotation]
        
        if direction == "down":
            self.block[2] += 1

            for i in range(len(block)):
                for j in range(len(block[i])):
                    if block[i][j] == "1":
                        self.filled_in.append((j + self.block[1], i + self.block[2]))
            
                
            for i in range(self.block[2],len(self.board)):
                for j in range(len(self.board[i])):
                    if (j,i) in self.filled_in:
                        self.blocks[(j,i)] = self.block[0]["color"]
        
        if direction == "right":
            self.block[1] += 1

            for i in range(len(block)):
                for j in range(len(block[i])):
                    if block[i][j] == "1":
                        self.filled_in.append((j + self.block[1],i + self.block[2]))
        
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if (j,i) in self.filled_in:
                        self.blocks[(j,i)] = self.block[0]["color"]
    
            
        if direction == "left":
            self.block[1] -= 1

            for i in range(len(block)):
                for j in range(len(block[i])):
                    if block[i][j] == "1":
                        self.filled_in.append((j + self.block[1],i + self.block[2]))
        
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if (j,i) in self.filled_in:
                        self.blocks[(j,i)] = self.block[0]["color"]
    
    def clear_row(self):
        inc = 0
        for i in range(len(self.board)):
            row = self.board[i]
            if (255,255,255) not in row:
                inc += 1
                ind = i
                for j in range(len(row)):
                    try:
                        del self.blocks_on_board[(j,i)] 
                    except:
                        continue
            if inc > 0:
                for key in sorted(list(self.blocks_on_board), key = lambda x: x[1])[::-1]:
                    x, y = key
                    if y < ind:
                        newKey = (x, y+ inc)
                        self.blocks_on_board[newKey] = self.blocks_on_board.pop(key)
            
                self.score += 10 



            
            #if inc > 0:
                #temp = {}
                #for block in self.blocks_on_board:
                    #if block[1] < ind:
                        #color = self.blocks_on_board[block]
                        #y = block[1] + 1
                        #x = block[0] 
                        #temp[(x,y)] = color
                    #temp[(block)] = (255,255,255)
                #self.blocks.clear()
                #self.blocks_on_board.clear()
                #for n in temp:
                    #self.blocks[n] = temp[n]
                    #self.blocks_on_board[n] = temp[n]
                
                #for block in self.blocks:
                    #if block[1] < ind:
                        #color = self.blocks[block]
                        #y = block[1] + 1
                        #x = block[0] 
                        #temp[(x,y)] = color
                        #temp[(block)] = (255,255,255)
                #self.blocks.clear()
                #for n in temp:
                    #self.blocks[n] = temp[n]
                    #self.blocks_on_board[n] = temp[n]
                
                #self.draw_board()
            

        
    
    def handle_events(self):
        while True:

            self.draw_board()
            pygame.display.flip()

            self.block_moves("down")
            self.clear_row()
            
            #font = pygame.font.SysFont("comicsans", 40, bold = True)
            #score = font.render(f"SCORE: {str(self.score)}", 1, (210, 150, 75))
            #self.display.blit(score, (600, 600))
            
            if not self._can_move():
                #self.clear_row()
                self._block_stop()
                self.change_block()
            self.draw_board()
            self.show_next_block()
            self._clock.tick(5)



            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.block_moves("down")
                    if event.key == pygame.K_RIGHT:
                        self.block_moves("right")
                    if event.key == pygame.K_LEFT:
                        self.block_moves("left")
                    if event.key == pygame.K_UP:
                        self.block_rotate()

                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    quit()
            



display1 = pygame.display.set_mode((600,700))
testi = GameLoop(display1)
block1 = Blocks()
testi.block_moves("down")
print(testi.blocks)

for block in testi.blocks:
    print(block, testi.blocks[block])
#test_block = block1.new_block
#print(testi.block_moves("down"))
#boardh = testi.draw_board()
#print(testi.block_rotate())
#print(testi.filled_in)
#print(testi.block[1])
#print(testi.block_moves("down"))

#print(3%2)
#print(1%2)
#print(2%2)

#for i in range(len(boardh)):
    #print(f"i: {i}")
    #for j in range(len(boardh[i])):
        #print("j:",j)