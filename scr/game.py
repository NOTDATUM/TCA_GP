class Game:
    def __init__(self, id):
        self.p1_info = [[200, 200], [200, 300], [200, 400], 0]
        self.p1_hp = [100, 100, 100]
        self.p2_info = [[200, 200], [200, 300], [200, 400], 0]
        self.p2_hp = [100, 100, 100]
        self.p1_bullets = []
        self.p2_bullets = []
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
    
    def bullet(self, player, cod_x, cod_y, number):
        if player == 1:
            if len(self.p1_bullets) > number:
                self.p1_bullets[number] = [cod_x, cod_y]
            else:
                self.p1_bullets.append([cod_x, cod_y])
        else:
            if len(self.p2_bullets) > number:
                self.p2_bullets[number] = [cod_x, cod_y]
            else:
                self.p2_bullets.append([cod_x, cod_y])

    def delete(self, player, number):
        if player == 1:
            self.p1_bullets.pop(number)
        else:
            self.p2_bullets.pop(number)
    
    def hit(self, player, number):
        if player == 1:
            self.p2_hp[number] -= 50
        else:
            self.p1_hp[number] -= 50
        
    
    def connected(self):
        return self.ready