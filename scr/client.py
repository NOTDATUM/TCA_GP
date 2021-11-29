from pickle import REDUCE
import pygame
from pygame.key import *
from network import Network
from module import *
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
slc = 0
n = Network()

pygame.font.init()

win = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Client")

def timepass(ob):
    ob.move()

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

    
def main():
    global n, slc
    run = True
    clock = pygame.time.Clock()
    player = int(n.getP())
    print(player)
    if player == 0:
        color = RED
        op_color = BLUE
    else:
        color = BLUE
        op_color = RED

    f = Person([200, 200], 1)
    s = Person([200, 300], 2)
    t = Person([200, 400], 3)

    while run:
        clock.tick(10000)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break
    
        win.fill(WHITE)
        if not(game.connected()):
            font = pygame.font.SysFont("Sans", 80)
            text = font.render("Logined", 1, (255,255,255), True)
            win.blit(text, (SCREEN_X/2 - text.get_width()/2, SCREEN_Y/2 - text.get_height()/2))
        else:
            Person.PersonList[slc].move()

            for i in range(len(Bullet.BulletList)):
                for j in range(3):
                    if distance(game.p2_info[j], Bullet.BulletList[i].loc) < 20:
                        n.send("hit "+str(i))

                Bullet.BulletList[i].move()
                n.send("bullet " + str(Bullet.BulletList[i].loc[0]) + " " + str(Bullet.BulletList[i].loc[1]) + " " + str(i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    Person.PersonList[slc].next(list(pygame.mouse.get_pos()))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    compare_distance, std_distance = 0, 0
                    for i in range(3):
                        if std_distance < distance(Person.PersonList[i].get_loc(), pygame.mouse.get_pos()):
                            std_distance = distance(Person.PersonList[i].get_loc(), pygame.mouse.get_pos())
                    compare_distance = std_distance
                    for i in range(3):
                        mouse_psn_distance = distance(Person.PersonList[i].get_loc(), pygame.mouse.get_pos())
                        if mouse_psn_distance < compare_distance and mouse_psn_distance < 15:
                            compare_distance = mouse_psn_distance
                            slc = i
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    Person.PersonList[slc].shoot(angle(Person.PersonList[slc].loc, pygame.mouse.get_pos()))
                            
            for i in range(len(Bullet.BulletList)):
                pygame.draw.circle(win, color, (Bullet.BulletList[i].loc[0], Bullet.BulletList[i].loc[1]), 3)
                n.send("delete " + str(Bullet.BulletList[i].check()))
            
            if player == 0:
                for j in range(len(game.p1_bullets)):
                    pygame.draw.circle(win, op_color, (game.p1_bullets[j][0], game.p1_bullets[j][1]), 3)
            else:
                for j in range(len(game.p2_bullets)):
                    pygame.draw.circle(win, op_color, (game.p2_bullets[j][0], game.p2_bullets[j][1]), 3)
            
            n.send("move "+str(Person.PersonList[slc].loc[0])+" "+ str(Person.PersonList[slc].loc[1])+" "+str(slc))
            if player == 0:
                if game.p1_hp[0]:
                    pygame.draw.circle(win, op_color, (game.p1_info[0][0], game.p1_info[0][1]), 20)
                if game.p1_hp[1]:
                    pygame.draw.circle(win, op_color, (game.p1_info[1][0], game.p1_info[1][1]), 20)
                if game.p1_hp[2]:
                    pygame.draw.circle(win, op_color, (game.p1_info[2][0], game.p1_info[2][1]), 20)
                if game.p2_hp[0]:
                    pygame.draw.circle(win, color, (Person.PersonList[0].loc[0], Person.PersonList[0].loc[1]), 20)
                if game.p2_hp[1]:    
                    pygame.draw.circle(win, color, (Person.PersonList[1].loc[0], Person.PersonList[1].loc[1]), 20)
                if game.p2_hp[2]:    
                    pygame.draw.circle(win, color, (Person.PersonList[2].loc[0], Person.PersonList[2].loc[1]), 20)
            else:
                if game.p2_hp[0]:
                    pygame.draw.circle(win, op_color, (game.p2_info[0][0], game.p2_info[0][1]), 20)
                if game.p2_hp[1]:    
                    pygame.draw.circle(win, op_color, (game.p2_info[1][0], game.p2_info[1][1]), 20)
                if game.p2_hp[2]:
                    pygame.draw.circle(win, op_color, (game.p2_info[2][0], game.p2_info[2][1]), 20)
                if game.p1_hp[0]:
                    pygame.draw.circle(win, color, (Person.PersonList[0].loc[0], Person.PersonList[0].loc[1]), 20)
                if game.p1_hp[1]:    
                    pygame.draw.circle(win, color, (Person.PersonList[1].loc[0], Person.PersonList[1].loc[1]), 20)
                if game.p1_hp[2]:    
                    pygame.draw.circle(win, color, (Person.PersonList[2].loc[0], Person.PersonList[2].loc[1]), 20)

        pygame.display.update()

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill(BLACK)
        font = pygame.font.SysFont("Sans", 60)
        text = font.render("Login", 1, (255, 255, 255))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()
