class Game:
    def __init__(self, id):
        self.p1_info = [[200, 200], [200, 300], [200, 400], 0]
        self.p2_info = [[200, 200], [200, 300], [200, 400], 0]
        self.ready = False
        self.id = id

    def move(self, player, cod_x, cod_y, number):
        if player == 1:
            self.p1_info[number][0] = cod_x
            self.p1_info[number][1] = cod_y
            self.p1_info[3] = number
        else:
            self.p2_info[number][0] = cod_x
            self.p2_info[number][1] = cod_y
            self.p2_info[3] = number
    
    def connected(self):
        return self.ready