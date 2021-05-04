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
        """ asettaa pelilaudan matriisin koordinaateille arvot eli rgb-värit
        """
        blocks = self.blocks
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (j,i) in self.blocks_on_board:
                    self.board[i][j] = self.blocks_on_board[(j,i)]
                elif (j,i) in blocks:
                    self.board[i][j] = blocks[(j,i)]


    def draw_board(self):
        """ piirtää pygamen näytölle pelilaudan sen koordinaattien arvojen mukaan
            sekä pelaajan senhetkiset pisteet
        """
        self.setup_board()

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                rect = (self._left_x + j * self._cell_size, self._top_y + i * self._cell_size,
                        self._cell_size, self._cell_size)
                pygame.draw.rect(self.display, self.board[i][j], rect ,0)

        rect = (600, 600, self._cell_size * 20, self._cell_size*20)
        pygame.draw.rect(self.display,(230,210,170), rect ,0)
        font = pygame.font.SysFont("comicsans", 40)
        score = font.render(f"SCORE: {self.score}", 1, (210, 150, 75))
        self.display.blit(score, (600, 600))
        pygame.display.flip()

    def _can_move(self):
        """ tarkistaa pystyykö tetris-pala liikkumaan menemättä pelilaudan reunojen yli

        Returns:
            boolean, joko voi liikkua tai ei
        """

        for pos in self.filled_in:
            if pos[0] > 20 or pos[0] < 0:
                return False
            if pos[1] > 28 or pos[1] < 0:
                return False

            if (pos[0], pos[1] + 1) in self.blocks_on_board:
                return False

        return True


    def block_stop(self):
        """ pysäyttää palan liikkumisen eli tallettaa sen arvot sanakirjaan,
        jossa on kaikki laudalla olevat palat
        """

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (j,i) in self.blocks and self.blocks[(j,i)] != (255,255,255):
                    self.blocks_on_board[(j,i)] = self.blocks[(j,i)]

        self.get_new_block = True

    def change_block(self):
        """ muodostaa uuden palan
        """
        self.block = self._next_block
        self._next_block = Blocks()
        self._next_block = self._next_block.new_block()
        self.get_new_block = False
        self.rotation = 0

    def show_next_block(self):
        """näyttää pelatessa mikä pala on seuraavana jonossa
        """
        rect = (600, 150, self._cell_size * 20, self._cell_size*20)
        pygame.draw.rect(self.display,(230,210,170), rect ,0)

        block = self._next_block
        next_block = []
        for i in range(len(block[0]["shape"][0])):
            for j in range(len(block[0]["shape"][0][i])):
                if block[0]["shape"][0][i][j] == "1":
                    next_block.append((j,i))

        for box in next_block:
            rect = (600 + box[0] * self._cell_size,  150 + box[1] * self._cell_size,
                    self._cell_size, self._cell_size)
            pygame.draw.rect(self.display, block[0]["color"], rect ,0)


    def block_rotate(self):
        """ kääntää palan
        """
        self.rotation += 1
        if self.rotation >= len(self.block[0]["shape"]):
            self.rotation = 0


    def block_moves(self, direction):
        """ liikuttaa palaa muuttamalla sen x ja y arvoja eli koordinaatteja
        Args:
            direction (str): mihin suuntaan palikka on liikkumassa
        """
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
        """tyhjentää rivin, kun se on täynnä sekä siirtää laudalle jäävät palat rivin alaspäin
        """
        n = 0
        for i in range(len(self.board)):
            row = self.board[i]
            if (255,255,255) not in row:
                n += 1
                ind = i
                for j in range(len(row)):
                    try:
                        del self.blocks_on_board[(j,i)]
                    except:
                        continue
            if n > 0:
                for key in sorted(list(self.blocks_on_board), key = lambda i: i[1])[::-1]:
                    i, j = key
                    if j < ind:
                        new_key = (i, j + n)
                        self.blocks_on_board[new_key] = self.blocks_on_board.pop(key)

                self.score += 10




    def handle_events(self):
        """ liikuttaa palikkaa kokoajan alaspäin
            ja valvoo pelin aikana tapahtuvia tapahtumia ja toimii niiden mukaan.
        """
        while True:

            self.draw_board()
            pygame.display.flip()

            self.block_moves("down")
            self.clear_row()

            if not self._can_move():
                self.block_stop()
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
