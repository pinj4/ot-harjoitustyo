class Board:
    def __init__(self, display):
        self.display = display
        self.board = []


    def tetris_board(self):
        """ muodostaa pelilaudan

        Returns:
            15 * 35 matriisi, jonka jokaisen jäsenen arvona (255,255,255) eli valkoinen
        """
        height = 35
        width = 15

        for i in range(height):
            row = []
            for j in range(width):
                row.append((255,255,255))
            self.board.append(row)
        return self.board
