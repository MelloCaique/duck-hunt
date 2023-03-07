import pygame as pg
import random
import math
from settings import *
from assets import *


class Hit:
    def __init__(self, game):
        self.game = game
        self.hit_duck = False
        self.screen = game.screen
        self.hit_points = 0

    def movement(self, duck_x, duck_y, aim_x, aim_y):
        keys = pg.key.get_pressed()
        # TODO let it more readable.
        d = math.sqrt(
            math.pow((aim_x - (duck_x + DUCK_RADIUS)), 2) + math.pow((aim_y - (duck_y + DUCK_RADIUS)), 2))
        if keys[pg.K_SPACE]:
            if DUCK_RADIUS > (d + AIM_RADIUS):
                self.hit_duck = True
            else:
                self.hit_duck = False

    def draw(self, duck_x, duck_y, aim_x, aim_y):
        font = pg.font.SysFont(None, 24)
        img = font.render(f' DUCK X:{duck_x:.1f}  Y:{duck_y:.1f}', True, 'red')
        self.screen.blit(img, (20, 20))
        img2 = font.render(f' AIM X:{aim_x:.1f}  Y:{aim_y:.1f}', True, 'red')
        self.screen.blit(img2, (20, 40))
        img3 = font.render(f' HIT: {self.hit_duck}', True, 'red')
        self.screen.blit(img3, (20, 60))
        img4 = font.render(f' POINTS: {self.hit_points}', True, 'red')
        self.screen.blit(img4, (20, 80))
        if self.hit_duck:
            pg.draw.circle(self.game.screen, 'blue', (700, 600), 30)
        else:
            pg.draw.circle(self.game.screen, 'yellow', (700, 600), 30)

    def update(self, duck_x, duck_y, aim_x, aim_y):
        self.movement(duck_x, duck_y, aim_x, aim_y)


