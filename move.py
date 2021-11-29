import math

DAMAGE = 7
TICK = 60
SHOTCOOLTIME = 85
MAXHP = 20
BULLETLOADS = 2


def angle(x_0, y_0, x, y):
    ang = 0  # -pi/2 ~ 3pi/2
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


class Person:
    PersonList = []

    def __init__(self, _x=400, _y=300, _v=1.5):
        self.pos, self.destination, self.v = [_x, _y], [_x, _y], _v
        self.no = len(Person.PersonList)
        Person.PersonList.append(self)
        self.maxhp, self.hp, self.bullets = MAXHP, MAXHP, BULLETLOADS
        self.cooltime = SHOTCOOLTIME

    def getpos(self):
        return self.pos

    def destinate(self, _x, _y):
        self.destination = [_x, _y]

    def move(self):
        ang = angle(*self.pos, *self.destination)
        if not((-1)*self.v <= self.destination[0] - self.pos[0] <= self.v):
            self.pos[0] += self.v * math.cos(ang) * 100 / 30
        if not((-1)*self.v <= self.destination[1] - self.pos[1] <= self.v):
            self.pos[1] += self.v * math.sin(ang) * 100 / 30

    def attacked(self):
        self.hp -= DAMAGE

    def shoot(self, ang):
        if self.bullets > 0:
            self.bullets -= 1
            self.cooltime = 0
            Bullet(*self.pos, ang, 30)

    def cooldown(self):
        if self.cooltime < SHOTCOOLTIME:
            self.cooltime += 1
        if self.cooltime == SHOTCOOLTIME and self.bullets < BULLETLOADS:
            self.bullets = BULLETLOADS
            if self.bullets < BULLETLOADS:
                self.cooltime = 0


class Bullet:
    BulletList = []

    def __init__(self, _x, _y, ang, _v=10000):
        self.pos, self.angle, self.v = [_x, _y], ang, _v
        Bullet.BulletList.append(self)

    def move(self):
        self.pos[0] += self.v * math.cos(self.angle) / 3.5
        self.pos[1] += self.v * math.sin(self.angle) / 3.5