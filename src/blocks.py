from random import choice

class Blocks():
    def __init__(self):
        self.j_block = {}
        self.l_block = {}
        self.s_block = {}
        self.square = {}
        self.stick = {}
        self.t_block = {}
        self.z_block = {}

        self.j_block["shape"] = [["0000",
                                "0001",
                                "0001",
                                "0011"],
                                ["0000",
                                "0000",
                                "1000",
                                "1110"],
                                ["0011",
                                "0010",
                                "0010",
                                "0000"],
                                ["0000",
                                "0000",
                                "0111",
                                "0001"]]
        self.j_block["color"] = (0,0,255)
        self.l_block["shape"] = [["0000",
                                "0010",
                                "0010",
                                "0011"],
                                ["1110",
                                "1000",
                                "0000",
                                "0000"],
                                ["0011",
                                "0001",
                                "0001",
                                "0000"],
                                ["0001",
                                "0111",
                                "0000",
                                "0000"]]
        self.l_block["color"] = (255, 255, 0)

        self.s_block["shape"] = [["0011",
                                "0110",
                                "0000",
                                "0000"],
                                ["0100",
                                "0110",
                                "0010"]]
        self.s_block["color"] = (0, 255, 0)

        self.square["shape"] = [["0011",
                                "0011",
                                "0000",
                                "0000"],
                                ["0011",
                                "0011",
                                "0000",
                                "0000"]]
        self.square["color"] = (255, 100, 180)

        self.stick["shape"] = [["0001",
                               "0001",
                               "0001",
                               "0001"],
                               ["1111",
                               "0000",
                               "0000",
                               "0000"]]
        self.stick["color"] = (0, 255, 255)

        self.t_block["shape"] = [["0000",
                                "0010",
                                "0011",
                                "0010"],
                                ["0000",
                                "0111",
                                "0010",
                                "0000"],
                                ["0000",
                                "0001",
                                "0011",
                                "0001"],
                                ["0000",
                                "0010",
                                "0111",
                                "0000"]]
        self.t_block["color"] = (240, 0, 255)

        self.z_block["shape"] = [["1100",
                                "0110",
                                "0000",
                                "0000"],
                                ["0010",
                                "0110",
                                "0100",
                                "0000"]]
        self.z_block["color"] = (255, 0, 0)

        self.blocks= [self.j_block, self.l_block, self.s_block,
                      self.square, self.stick, self.t_block, self.z_block]

    def new_block(self):
        """ muodostaa block-olion

        Returns:
            lista, jonka arvoina on block-olio, arvo x ja arvo y
        """
        block_type = choice(self.blocks)
        j = 0
        i = 0
        block = [block_type, j, i]
        return block
