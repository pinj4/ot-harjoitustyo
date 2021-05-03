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
        self.j_block["color"] = (0,0,255) # blue
        
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
        self.l_block["color"] = (255, 255, 0) # yellow ?
        
        self.s_block["shape"] = [["0011",
                                "0110",
                                "0000",
                                "0000"],
                                ["0100",
                                "0110",
                                "0010"]]                                
        self.s_block["color"] = (0, 255, 0) # green

        self.square["shape"] = [["0011",
                                "0011",
                                "0000",
                                "0000"],
                                ["0011",
                                "0011",
                                "0000",
                                "0000"]]
        self.square["color"] = (255, 100, 180) # pink

        self.stick["shape"] = [["0001",
                               "0001",
                               "0001",
                               "0001"],
                               ["1111",
                               "0000",
                               "0000",
                               "0000"]]
        self.stick["color"] = (0, 255, 255) # light blue

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
        self.t_block["color"] = (240, 0, 255) # purple ??
        
        self.z_block["shape"] = [["1100",
                                "0110",
                                "0000",
                                "0000"],
                                ["0010",
                                "0110",
                                "0100",
                                "0000"]]
        self.z_block["color"] = (255, 0, 0) # red
         
        self.blocks= [self.j_block, self.l_block, self.s_block, 
                      self.square, self.stick, self.t_block, self.z_block]
        
    def new_block(self):
        block_type = choice(self.blocks)
        x = 0
        y = 0
        block = [block_type, x, y]
        return block

#test_block = Blocks()
#block1 = test_block.new_block()
#print(block1[0]["shape"][0][0],block1[0]["shape"][1])
#print(block1)

#block = block1[0]["shape"][0]

#for i in range(len(block)):
    #for j in range(len(block[i])):
        #print(block[i][j], "i,j",(j,i))






        


        


        

        


    
            

   

    

