import pygame
from move import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game name')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 7)
running = True

move_event = pygame.key.get_pressed()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SKYBLUE = (100, 100, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

a = Person()
a.attacked()


def timepass():
    a.cooldown()
    a.move()
    for bul in Bullet.BulletList:
        bul.move()


while running:
    dt = clock.tick(TICK)
    timepass()
    screen.fill(BLACK)
    pygame.draw.polygon(screen, BLUE, [[a.getpos()[0]-10, a.getpos()[1]-10], [a.getpos()[0]+10, a.getpos()[1]-10], [a.getpos()[0]+10, a.getpos()[1]+10], [a.getpos()[0]-10, a.getpos()[1]+10]], 0)
    pygame.draw.rect(screen, GREEN, [a.getpos()[0]-13, a.getpos()[1]-17, 26*a.hp/a.maxhp, 4], 0)
    pygame.draw.rect(screen, RED, [a.getpos()[0] - 13 + 26*a.hp/a.maxhp, a.getpos()[1] - 17, 26 - 26*a.hp/a.maxhp, 4], 0)
    pygame.draw.rect(screen, SKYBLUE, [a.getpos()[0] - 13, a.getpos()[1] - 22, 26, 3], 1)
    pygame.draw.rect(screen, SKYBLUE, [a.getpos()[0] - 13, a.getpos()[1] - 22, 26 * a.cooltime / SHOTCOOLTIME, 3], 0)
    if BULLETLOADS == 2:
        if a.bullets > 0:
            pygame.draw.rect(screen, WHITE, [a.getpos()[0] - 5, a.getpos()[1] - 26, 2, 2], 0)
        if a.bullets > 1:
            pygame.draw.rect(screen, WHITE, [a.getpos()[0] + 5, a.getpos()[1] - 26, 2, 2], 0)
        pygame.draw.rect(screen, SKYBLUE, [a.getpos()[0] - 13, a.getpos()[1] - 22, 26 * a.cooltime / SHOTCOOLTIME, 3], 0)
    # if BULLETLOADS == 3:
    #     if a.bullets > 0:
    #         pygame.draw.rect(screen, WHITE, [a.getpos()[0] - 5, a.getpos()[1] - 26, 2, 2], 0)
    #     if a.bullets > 1:
    #         pygame.draw.rect(screen, WHITE, [a.getpos()[0], a.getpos()[1] - 26, 2, 2], 0)
    #     if a.bullets > 2:
    #         pygame.draw.rect(screen, WHITE, [a.getpos()[0] + 5, a.getpos()[1] - 26, 2, 2], 0)
    # if BULLETLOADS == 4:
    #     if a.bullets > 0:
    #         pygame.draw.rect(screen, WHITE, [a.getpos()[0] - 7, a.getpos()[1] - 26, 2, 2], 0)
    #     if a.bullets > 1:
    #         pygame.draw.rect(screen, WHITE, [a.getpos()[0] - 3, a.getpos()[1] - 26, 2, 2], 0)
    #     if a.bullets > 2:
    #         pygame.draw.rect(screen, WHITE, [a.getpos()[0] + 1, a.getpos()[1] - 26, 2, 2], 0)
    #     if a.bullets > 3:
    #         pygame.draw.rect(screen, WHITE, [a.getpos()[0] + 5, a.getpos()[1] - 26, 2, 2], 0)

    for bul in Bullet.BulletList:
        pygame.draw.circle(screen, WHITE, bul.pos, 3, 0)

    pygame.draw.rect(screen, SKYBLUE, [a.getpos()[0] - 13, a.getpos()[1] - 22, 26 * a.cooltime / SHOTCOOLTIME, 3], 0)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # 마우스 클릭 시 십자가 모양 z
            a.destinate(*list(pygame.mouse.get_pos()))
            pygame.draw.rect(screen, WHITE, [pygame.mouse.get_pos()[0] - 1, pygame.mouse.get_pos()[1] - 5, 2, 10], 0)
            pygame.draw.rect(screen, WHITE, [pygame.mouse.get_pos()[0] - 5, pygame.mouse.get_pos()[1] - 1, 10, 2], 0)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            a.shoot(angle(*a.getpos(), *pygame.mouse.get_pos()))
