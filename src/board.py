class Board:
    def __init__(self, display):
        self.display = display
        self.board = []


    def tetris_board(self):
        height = 40
        width = 20

        for y in range(height):
            row = []
            for x in range(width):
                row.append((255,255,255))
            self.board.append(row)
        return self.board








    
    











