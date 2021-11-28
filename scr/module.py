import math

MAX_HP = 100
DAMAGE = 10
MAX_BULLET = 2
SHOT_COOLTIME = 100
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

def distance(p_1, p_2):  # 두 점 사이 거리 반환
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
        self.bts = MAX_BULLET
        self.ctm = SHOT_COOLTIME
        self.isW = False
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
        if self.bts > 0:
            self.bts -= 0
            self.ctm = 0
            Bullet(self.get_loc(), ang, 30)

class Bullet:
    BulletList = []

    def __init__(self, init, angle, v):
        self.loc = init
        self.ang = angle
        self.v = v
        Bullet.BulletList.append(self)

    def move(self):
        self.pos[0] += self.v * math.cos(self.angle) / 3.5
        self.pos[1] += self.v * math.sin(self.angle) / 3.5