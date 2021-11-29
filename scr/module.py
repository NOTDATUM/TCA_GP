import math

MAX_HP = 100
DAMAGE = 10
SCREEN_X = 1200
SCREEN_Y = 750
SPEED = 1.5

def angle(p_0, p):  # p_0에서 p까지 측정한 각도, 범위는 -pi/2 ~ 3pi/2
    x_0, y_0, x, y, ang = p_0[0], p_0[1], p[0], p[1], 0
    if x - x_0 != 0 and y - y_0 != 0:
        if x_0 - x == 0:
            if y_0 - y > 0:
                ang = math.pi / 2
            if y_0 - y < 0:
                ang = (-1) * math.pi / 2
        if x - x_0 > 0:
            ang = math.atan((y_0 - y) / (x_0 - x))
        if x - x_0 < 0:
            ang = math.atan((y_0 - y) / (x_0 - x)) + math.pi
    return ang

def distance(p_1, p_2):
    return ((p_1[0] - p_2[0]) ** 2 + (p_1[1] - p_2[1]) ** 2) ** 0.5

class Person:
    PersonList = []

    def __init__(self, init, id):
        Person.PersonList.append(self)
        self.id = id
        self.loc = [init[0], init[1]]
        self.nex = [init[0], init[1]]
        self.hp = MAX_HP
        self.dmg = DAMAGE
        self.v = SPEED

    def next(self, next):
        self.nex = next

    def move(self):
        ang = angle(self.get_loc(), [self.nex[0], self.nex[1]])
        if not((-2) * self.v <= self.nex[0] - self.loc[0] <= 2 * self.v):
            self.loc[0] += self.v * math.cos(ang)
        if not((-2) * self.v <= self.nex[1] - self.loc[1] <= 2 * self.v):
            self.loc[1] += self.v * math.sin(ang)

    def get_loc(self):
        return self.loc

    def shoot(self, ang):
        Bullet(*self.loc, ang, 10)

class Bullet:
    BulletList = []

    def __init__(self, x, y, angle, v):
        self.loc = [x, y]
        self.angle = angle
        self.v = v
        self.no = len(Bullet.BulletList)
        Bullet.BulletList.append(self)

    def move(self):
        self.loc[0] += self.v * math.cos(self.angle)
        self.loc[1] += self.v * math.sin(self.angle)
    
    def check(self):
        if self.loc[0] < 0 or self.loc[0] > SCREEN_X or self.loc[1] < 0 or self.loc[1] > SCREEN_Y:
            number = self.no
            del self
            return number
        else:
            return "none"