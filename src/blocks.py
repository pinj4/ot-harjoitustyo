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

        self.j_block["shape"] = [[0,0,0,0],
                                [0,0,0,1],
                                [0,0,0,1],
                                [0,0,1,1]]
        self.j_block["color"] = (0,0,255) # blue
        
        self.l_block["shape"] = [[0,0,0,0],
                                [0,0,1,0],
                                [0,0,1,0],
                                [0,0,1,1]]
        self.l_block["color"] = (255, 255, 0) # yellow ?
        
        self.s_block["shape"] = [[0,0,1,1],
                                [0,1,1,0],
                                [0,0,0,0],
                                [0,0,0,0]]
        self.s_block["color"] = (0, 255, 0) # green

        self.square["shape"] = [[0,0,1,1],
                                [0,0,1,1],
                                [0,0,0,0],
                                [0,0,0,0]]
        self.square["color"] = (255, 100, 180) # pink

        self.stick["shape"] = [[0,0,0,1],
                               [0,0,0,1],
                               [0,0,0,1],
                               [0,0,0,1]]
        self.stick["color"] = (0, 255, 255) # light blue

        self.t_block["shape"] = [[0,0,0,0],
                                [0,0,1,0],
                                [0,0,1,1],
                                [0,0,1,0]]
        self.t_block["color"] = (240, 0, 255) # purple ??
        
        self.z_block["shape"] = [[1,1,0,0],
                                [0,1,1,0],
                                [0,0,0,0],
                                [0,0,0,0]]
        self.z_block["color"] = (255, 0, 0) # red
         
        self.blocks= [self.j_block, self.l_block, self.s_block, 
                      self.square, self.stick, self.t_block, self.z_block]
        
    def new_block(self):
        block_type = choice(self.blocks)
        x = 0
        y = 0
        block = [block_type, x, y]
        return block





        


        


        

        


    
            

   

    

